from collections import defaultdict
from operator import attrgetter
import datetime
import hashlib
import os
import logging
import sys

from lxml import etree
from lxml import objectify

from smdx import SMDX
from smdx import SMDXPoint as SP


# logger = logging.getLogger('ped.ssd')


class SunSpecData(object):
    element_name = 'sunSpecData'

    def __init__(self, element):
        '''Initialize a SunSpecData object given the XML Element
        '''
        self.element = element
        if self.element is None:
            self.exists = False
            return
        else:
            self.exists = True

        # check for sunSpecData version, assume '1' if absent
        v = self.element.get('v')
        if (v is not None):
            self.version = int(v)
        else:
            self.version = 1

        self.device_records = list()
        for d_record in self.element.iter(DeviceRecord.element_name):
            self.device_records.append(DeviceRecord(d_record))

        self.parsed = False

    def parse(self):
        logging.debug("SunSpecData.parse()")
        for dr in self.device_records:
            dr.parse()
        self.parsed = True

    def get_points(self):
        all_points = list()
        for dr in self.device_records:
            for model in dr.models:
                all_points = all_points + model.points
        return all_points

    def _get_matching_points(self, point_id):
        '''Get a list of points which match the given point_id
        '''
        points = list()
        logging.debug(''.join(["SunSpecData.get_matching_points() looking for point_id:",
                      str(point_id)]))
        for dr in self.device_records:
            models = dr.models
            if models is not None:
                for m in models:
                    plist = m.get_matching_points(point_id)
                    if (plist is not None) and plist:
                        points = points + plist
        return points

    def get_points_in_period(self, start_time, end_time, point_id='All'):
        '''Get a Point.time sorted list of points that are between the start_time
           and end_time and that match the point_id.

           If both start_time and end_time are None, then points for the sunSpecData
           block's entire time range are returned.

           Arguments:
           start_time -- the datetime describing the beginning of the period
           end_time -- the datetime describing the end of the period
           point_id -- the id of the Points to retrieve within the period

           Return:
           Points within the period as time sorted Points in a list
        '''
        logging.info("SunSpecData.get_points_in_period: " + str(start_time) +
                     " > " + str(end_time) + " point_id: " + point_id)

        if point_id is 'All':
            points = self.get_points()
        else:
            points = self._get_matching_points(point_id)

        period_points = list()
        for p in points:
            if (end_time is None) and (start_time is None):
                period_points.append(p)
            elif start_time < p.time < end_time:
                period_points.append(p)
        logging.info('Period points:', str(period_points))
        period_points = sorted(period_points, key=attrgetter('time'))
        return period_points

    def tostring(self):
        return ''.join(['SunSpecData v:', str(self.version),
                        ' point count: ', str(len(self.get_points()))])


class DeviceRecord(object):
    element_name = 'd'

    def __init__(self, element):
        element = element
        if element is None:
            logging.warning("DeviceRecord.__init__() element provided is None")
            return

        self.manufacturer = get_attr(element, 'man')
        self.model = get_attr(element, 'mod')
        self.serial_number = get_attr(element, 'sn')
        self.logger_id = get_attr(element, 'lid')
        self.logger_id_namespace = get_attr(element, 'ns')
        self.device_interface_id = get_attr(element, 'if')
        self.device_id = get_attr(element, 'id')
        self.correlation_id = get_attr(element, 'cid')

        self._determine_id()
        time = get_attr(element, 't')
        if time is None:
            raise SunSpecDataException("DeviceRecord 't' attribute is required.")
        else:
            # SunSpecData <d ... t="YYYY-MM-DDThh:mm:ssZ"
            self.time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')

        self.models = list()
        for m in element.iter(Model.element_name):
            m_id = m.get('id')
            if (m_id is not None):
                logging.debug("DeviceRecord.__init__() adding model_id: " + m_id)
                self.models.append(Model(m, m_id, self.time))

    def _determine_id(self):
        self.device_id_type = None
        gs = None
        if self.model and self.manufacturer and self.serial_number:
            gs = "" + self.serial_number + self.model + self.manufacturer
            self.device_id_type = 'Common Block'
        elif self.logger_id and self.device_id:
            gs = "" + self.device_id + self.logger_id
            self.device_id_type = 'Logger-specific, user-assigned'

        if gs is None:
            s = "A Device must have a globally unique identifier, either man: mod: sn: or lid: id:"
            raise SunSpecDataException(s)

        self.guid = int(hashlib.md5(gs).hexdigest(), 16)
        return

    def parse(self):
        logging.debug("SunSpecData.DeviceRecord.parse()")
        for model in self.models:
            model.parse()

    def tostring(self):
        return ''.join(["Device", os.linesep, " id_type:", self.device_id_type, " guid:",
                        str(self.guid), os.linesep, " man:", self.manufacturer,
                        " mod:", self.model, " sn:", self.serial_number, os.linesep,
                        " lid:", self.logger_id, " ns:", self.logger_id_namespace,
                        " id:", self.device_id, os.linesep, " if:",
                        self.device_interface_id, " cid:", self.correlation_id])


class Model(object):
    element_name = 'm'

    def __init__(self, element, id, dr_time):
        self.dr_time = dr_time
        self.points = list()
        if (element is None):
            raise SunSpecDataException("SunSpec model element is required for a Model")
        else:
            self.element = element

        if (id is None):
            raise SunSpecDataException("SunSpec model element must have an id attribute")
        else:
            self.id = int(id)

        self.smdx = SMDX(element, id)

    def parse(self):
        logging.debug("Model.parse() model_id:" + str(self.id))

        logging.info("Model.parse() instantiating Points")
        for p in self.element.iter(Point.element_name):
            self.points.append(Point(self, p))

        smdx_points = self.smdx.get_points()
        logging.info("Model.parse() adding units from SMDXPoints to Points")
        for p in self.points:
            if p.id in smdx_points:
                logging.info("Point.id:" + str(p.id) + " found in SMDX.model_id: " + str(self.id))
                p.units = smdx_points[p.id].units
                p.set_type(smdx_points[p.id].type)
                logging.info("Point.id:" + str(p.id) + " assigned units: " + str(p.units) +
                             " type:" + str(p.type))
            else:
                logging.warning(''.join(["Point.id:", str(p.id),
                                " exists but shouldn't for SMDX.model_id: ", str(self.id)]))

        mand_met = False
        if (len(self._has_mandatory_points()) == 0):
            mand_met = True
        logging.debug("Model.parse() has all mandatory points? " + str(mand_met))

    def get_matching_points(self, point_id):
        '''Get a list of points which match the given point_id
        '''
        points = list()
        logging.info(''.join(["Model.get_matching_points() looking for point_id:",
                     str(point_id)]))
        for p in self.points:
            logging.debug(''.join(["Model.get_matching_points() p.id:", p.id,
                                   " given point_id:", str(point_id)]))
            if p.id == point_id:
                points.append(p)
        return points

    def _has_mandatory_points(self):
        man_points = self.smdx.get_mandatory_points()
        points = self.points
        logging.debug("Model._has_mandatory_points()")
        missing_mand = {}

        for sp in man_points.itervalues():
            if sp.mandatory:
                found = False
                for p in points:
                    if sp.id == p.id:
                        logging.info("Found mandatory point:" + str(p.id))
                        found = True
                        break

                if not found:
                    logging.warning("Model.id:" + str(self.id) +
                                    " missing mandatory SMDXPoint.id:" + sp.id)
                    missing_mand[sp.id] = sp
        return missing_mand

    def set_metadata(self, element):
        return

    def tostring(self):
        return ''.join(['Model.id:', str(self.id), ' dr_time:', str(self.dr_time)])


class Point(object):
    element_name = 'p'

    def __init__(self, model, element):
        self.model = model
        element = element
        self.id = element.get('id')
        self.x = element.get('x')
        self.value = element.text
        self.units = None
        self.type = None

        time = element.get('t')
        if time is None:
            self.time = model.dr_time
        else:
            # SunSpecData <p ... t="YYYY-MM-DDThh:mm:ssZ"
            self.time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')

    def set_type(self, type):  # change to python attribute oriented setter!
        self.type = type
        logging.info("Point.set_type() id:", self.id, " type:", self.type)
        if (self.type == SP.UINT16) or (self.type == SP.INT16) or (self.type == SP.INT32):
            self.value = int(self.value)
        elif self.type == SP.FLOAT32 or self.type == SP.ACC32:
            self.value = float(self.value)
        return

#     def __radd__(self, other):
#         result = None
#         if (self.type == SP.UINT16) or (self.type == SP.INT16) or (self.type == SP.INT32):
#             print self.tostring()
#             if (other is not None):
#                 result = other + int(self.value)
#             else:
#                 result = int(self.value)
#         elif self.type == SP.FLOAT32:
#             if (other is not None):
#                 return other + float(self.value)
#             else:
#                 return float(self.value)
#         return result
#
#     def __add__(self, other):
#         if self.type == SP.UINT16 or SP.INT16 or SP.INT32:
#             result = int(self.value) + other
#         elif self.type == SP.FLOAT32:
#             result = float(self.value) + other
#         return result

    def tostring(self):
        return ''.join(['Point.id:', self.id, ' x:', str(self.x), ' value:',
                        str(self.value), ' units:', str(self.units), ' type:',
                        str(self.type), ' time:', str(self.time)])


class SunSpecDataException(Exception):

    def __init__(self, argument):
        super(SunSpecDataException, self).__init__(argument)
        self.argument = argument


####################
# Utility functions
def get_attr(element, attr_name):
    attr_value = None
    if element is None:
        return attr_value
    elif element.get(attr_name):
        attr_value = element.get(attr_name)
    return attr_value
