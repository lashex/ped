# coding=utf-8
# Copyright 2013 Gridward LLC
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from operator import attrgetter
import datetime as dt
import logging
import plant_extract_pyxb


time_format = '%Y-%m-%dT%H:%M:%SZ'
#   logger = logging.getLogger('ped') f =
#   logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s') sh =
#   logging.StreamHandler() sh.setFormatter(f) logger.addHandler(sh)


class PlantExtractParser(object):
    """ A Plant Extract Document processor supporting straightforward
        interaction with information from each of the standard blocks.
    """

    def __init__(self):
        logging.debug("PlantExtract.__init__()")
        self.ped = None

    def parse(self, ped_file):
        """Parse the plant extract document"""
        self.ped = plant_extract_pyxb.CreateFromDocument(
            open(ped_file).read(), location_base=ped_file
        )

        # TODO: sunSpecMetadata
        # TODO: strings
        # TODO: extract extensions
        return

    def __str__(self):
        """Produces a string representation of the Plant Extract envelope"""
        return ''.join(['PlantExtract v:', str(self.ped.v), ' t:', str(self.ped.t),
                        ' seqId:', str(self.ped.seqId), ' lastSeqId:', str(self.ped.lastSeqId)])

    def _matching_points(self, models, model_id, device_time, point_ids = None):
        """Get a list of sunSpecData Points which match the given point_ids.

        @param models: the Models from which to obtain matched Points
        @param model_id: the model_id of the Model to match Points
        @param device_time:
        @param point_ids: the Point ID list of Points to be retrieved.
        If 'None' then ALL Points on the Model are returned.
        @return matched_points: the matched points
        """
        points = list()
        if models is not None:
            for m in models:
                if m.id == model_id:
                    if point_ids is None:
                        # just add all points on the Model
                        logging.debug('_matching_points() adding all Points')
                        points.extend(m.p)
                    else:
                        for p in m.p:
                            logging.debug(''.join(["_matching_points() p.id:", p.id,
                                                   " given point_id:", str(point_ids)]))
                            if p.id in point_ids:
                                logging.debug(''.join(['_matching_points() found p.id:',
                                                       p.id]))
                                if p.t is None:
                                    # if Point time value 't' is None then inherit
                                    # device's time
                                    p.t = device_time
                                points.extend([p])
        return points

    def composite_points(self, model_id, man, mod, sn, point_ids):
        points = list()
        for dr in self.ped.sunSpecData.d:
            if dr.man == man and dr.mod == mod and dr.sn == sn:
                plist = self._matching_points(dr.m, model_id, device_time=dr.t,
                                              point_ids=point_ids)
                points.extend(plist)

        return points

    def logger_points(self, model_id, logger_id, point_ids):
        points = list()
        for dr in self.ped.sunSpecData.d:
            if dr.lid == logger_id:
                plist = self._matching_points(dr.m, model_id, device_time=dr.t,
                                              point_ids=point_ids)
                points.extend(plist)

        return points

    def device_points(self, model_id, device_id, point_ids):
        points = list()
        for dr in self.ped.sunSpecData.d:
            if dr.id == device_id:
                plist = self._matching_points(dr.m, model_id, device_time=dr.t,
                                              point_ids=point_ids)
                points.extend(plist)

        return points

    def model_points(self, model_id, point_ids):
        points = list()
        for dr in self.ped.sunSpecData.d:
            plist = self._matching_points(dr.m, model_id, device_time=dr.t,
                                          point_ids=point_ids)
            points.extend(plist)

        return points

    def last(self):
        """Determines if this Plant Extract is the last extract in a set
        """
        return self.ped.seqId == self.ped.lastSeqId

    def match_model_points(self, model_id, device_id=None, logger_id=None,
                           man=None, mod=None, sn=None, point_ids=None):
        """Get matched points for the given model_id.

        Additional parameter matching precedence is as follows:
          # device_id if present
          # man/mod/sn composite id if all present
          # logger_id if present
        Then if the Device matches the additional parameter precedence filter,
        model_id of any contained Models is checked. Finally the point_ids will
        act as a filter for any Points retrieved from the matching Model.
        @note If a matched Point did not have a timestamp the timestamp is
        inherited from the Device.

        @param model_id: the model ID from which to retrieve the Points
        @param device_id: the optional logger-defined Device ID. If the device
        ID is present, only Points from the model_id *and* device_id will be
        returned the man/mod/sn combination and logger_id will be ignored.
        @param man: the manufacturer of the device, used in the man/mod/sn
        composite Device ID
        @param mod: the model of the device, used in the man/mod/sn composite
        Device ID
        @param sn: the serial number of the device, used in the man/mod/sn
        composite Device ID
        @param logger_id: the optional logger ID of the Device. If the logger ID
        is present, only Points from the matching model_id *and* logger_id will
        be returned.
        @param point_ids: the optional Point ID list of Points to be retrieved.
        @return matched_points: the matched points
        """
        if model_id is None:
            return  # should throw exception
        else:
            model_id = str(model_id)

        points = None
        filter_by_id = None
        if device_id is None:
            if man is not None and mod is not None and sn is not None:
                logging.debug(''.join(['match_model_points composite id:',
                              man, mod, sn]))
                points = self.composite_points(model_id=model_id, man=man,
                                               mod=mod, sn=sn,
                                               point_ids=point_ids)
                return points
            elif logger_id is not None:
                logging.debug(''.join(['match_model_points logger_id:',
                              logger_id]))
                points = self.logger_points(model_id=model_id,
                                            logger_id=logger_id,
                                            point_ids=point_ids)
                return points
        else:
            logging.debug(''.join(['match_model_points device_id:',
                                   device_id]))
            points = self.device_points(model_id=model_id,
                                          device_id=device_id,
                                          point_ids=point_ids)
            return points

        logging.debug(''.join(['match_model_points model_id:',
                               model_id]))
        return self.model_points(model_id = model_id, point_ids=point_ids)


    def points_in_period(self, start_time, end_time, model_id, device_id=None,
                         logger_id=None, man=None, mod=None, sn=None,
                         point_ids=None):
        """ Get a Point.time sorted list of points that are between the start_time
            and end_time and that match the given criteria.

            If both start_time and end_time are None, then points for the
            sunSpecData block's entire time range is returned.
            @see get_matched_points_for_model for parameter matching precedence.

            @requires start_time: the datetime describing the beginning of the period
            @requires end_time: the datetime describing the end of the period
            @requires model_id: the model ID from which to retrieve the Points
            @param device_id: the optional logger-defined Device ID. If the device
            ID is present, only Points from the model_id *and* device_id will be
            returned the man/mod/sn combination and logger_id will be ignored.
            @param man: the manufacturer of the device, used in the man/mod/sn
            composite Device ID
            @param mod: the model of the device, used in the man/mod/sn composite
            Device ID
            @param sn: the serial number of the device, used in the man/mod/sn
            composite Device ID
            @param logger_id: the optional logger ID of the Device. If the logger ID
            is present, only Points from the matching model_id *and* logger_id will
            be returned.
            @param point_ids: the optional Point ID list of Points to be retrieved.

            @return period_points: points within the period as time sorted
            Points in a list
        """
        logging.info("points_in_period: "+str(start_time)+" > "+str(end_time))

        points = list()
        points.extend(self.match_model_points(model_id, device_id=device_id,
                                              logger_id=logger_id,
                                              man=man, mod=mod, sn=sn,
                                              point_ids=point_ids))

        period_points = list()
        if end_time is None and start_time is None:
            period_points.extend(points)
        else:
            if end_time is None:
                # if end_time is None then treat that as implying "now"
                et = dt.datetime.utcnow()
            else:
                et = dt.datetime.strptime(end_time, time_format)

            if start_time is None:
                st = dt.datetime.MINYEAR
            else:
                st = dt.datetime.strptime(start_time, time_format)

            for p in points:
                pt = dt.datetime.strptime(p.t.value(), time_format)
                if st < pt < et:
                    period_points.extend(p)

        logging.info('points_in_period point count: '+str(len(period_points)))
        period_points = sorted(period_points, key=attrgetter('t'))
        return period_points


class ModelIDValues(object):
    # list of convenient model id values
    # Common block Model IDs
    COMMON = 1
    AGGREGATOR = 2

    # Inverter Model IDs
    INVERTER_SINGLE_PHASE = 101
    INVERTER_SPLIT_PHASE = 102
    INVERTER_THREE_PHASE = 103

    # Meter Model IDs
    METER_SINGLE_PHASE = 201

    # Environmental Model IDs
    ENV_IRRADIANCE = 302
    ENV_BOM_TEMPERATURE = 303

class PointIDValues(object):
    # list of convenient point ID values
    MANUFACTURER = 'Mn'
    MODEL = 'Md'

    ENERGY = 'WH'
    TOTAL_ENERGY_EXPORTED = 'TotWhExp'
    TOTAL_ENERGY_IMPORTED = 'TotWhImp'
    POWER = 'W'
    GLOBAL_HORIZONTAL_IRRADIANCE = 'GHI'
    PLANE_OF_ARRAY_IRRADIANCE = 'POAI'
    DIFFUSE_IRRADIANCE = 'DFI'
    BOM_TEMPERATURE = 'TmpBOM'

    FLOAT32 = 'float32'
    INT16 = 'int16'
    UINT16 = 'unint16'
    INT32 = 'int32'
    ACC16 = 'acc16'
    ACC32 = 'acc32'

    # TODO utility method to convert list of Points to have SMDX types
    #@classmethod
    #def spec_points(self, points):
    #    """Convert given list of Points to have SunSpec SMDX compliant types.
    #    :param points: the list of Points to process
    #    :return points: Points with their type now compliant with SunSpec SMDX
    #    """
    #    logging.info("Point.spec_points() id:", self.id, " type:", self._type)
    #    for point in points:
    #        if (point. == PointIDValues.UINT16 or
    #            self._type == PointIDValues.INT16
    #            or self._type == SP.INT32 or self._type == SP.ACC16
    #            or self._type == SP.ACC32):
    #            self.value = int(self.value)  # Convert into 32 bit signed
    #        elif self._type == SP.FLOAT32:
    #            self.value = float(self.value)   # Convert into 64 bit float

