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

from uuid import UUID
from uuid import uuid4
from collections import defaultdict
import logging
import datetime as dt
import json

from sunspec import SunSpecData

# TODO move all parsing out into PlantParser, LocationParser, etc... which will
# TODO clean up the core objects.

time_format = '%Y-%m-%dT%H:%M:%SZ'
logger = logging.getLogger('ped')
f = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
sh = logging.StreamHandler()
sh.setFormatter(f)
logger.addHandler(sh)


class PlantExtract(object):
    """ A Plant Extract Document
    """
    def __init__(self, plant, seqId='1', lastSeqId='1', ssd=None):
        """Create a plant extract document given parameters and data for the
           standard blocks.
        :param plant: a Plant object with at least a PlantID
        :param ssd: a sunspec_data.DeviceRecord[]
        """
        logger.debug("PlantExtract.create()")
        self.version = '2'
        self.seqId = seqId
        self.lastSeqId = lastSeqId
        self.time = dt.datetime.utcnow().strftime(time_format)
        self.plant = plant

    def __str__(self):
        """Produces a string representation of the Plant Extract envelope"""
        return ''.join(['PlantExtract v:', str(self.version), ' t:', str(self.time),
                        ' seqId:', str(self.seqId), ' lastSeqId:', str(self.lastSeqId)])

    def last(self):
        """Determines if this Plant Extract is the last extract in a set
        """
        return self.seqId == self.lastSeqId

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)


class Plant(object):
    def __init__(self, plant_id, locale="en-US", name="", notes="",
               description="", activation_date=None, location=None,
               name_plate=None, design_elements=None, array=None,
               equipment=None):
        """

        :param plant_id: a UUID4 that uniquely identifies the plant, required
        :param locale:
        :param name:
        :param notes:
        :param description:
        :param activation_date: the date the power plant was actively
            delivering power to the utility grid or energy off-taker. The
            activation_date value must be compliant with the ISO 8601 date
            format: "YYYY-MM-DD”
        :param location:
        :param name_plate:
        :param design_elements:
        :param array: a list of elements that describe the attributes of a PV
            array
        :param equipment:
        :return:
        """
        self.version = 2
        self.plant_id = plant_id
        self.locale = locale
        self.name = name
        self.notes = notes
        self.description = description
        if activation_date is not None:
            # validate given activation date complies with format
            ad = dt.datetime.strptime(activation_date, '%Y-%m-%d')
            # convert back into string
            self.activation_date = ad.strftime('%Y-%m-%d')

        self.location = location
        self.name_plate = name_plate
        self.design_elements = design_elements
        self.array = array
        self.equipment = equipment

    def __str__(self):
        """Produces a string representation of some parsed Plant values """
        return ''.join(["Plant id:", self.plant_id, ", v:", str(self.version),
                        ", name:", self.name, ", locale:", self.locale,
                        ", description:", self.description])

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)


class PropertyContainer(object):
    def __init__(self, props):
        #self.properties = defaultdict(list)
        self.properties = {}
        for p in props:
            self.properties[p.prop_id] = p

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2)

    def __str__(self):
        pc = ''
        for k in self.properties:
            pc += str(self.properties[k]) + ' '
        return pc

class Property(object):
    def __init__(self, prop_id, prop_type, text):
        self.prop_id = prop_id
        self.type = prop_type
        self.text = text

    def __str__(self):
        return ''.join(['Property prop_id:', str(self.prop_id), ', type:',
                        str(self.type), ', text:', str(self.text)])


class Location(PropertyContainer):
    def __init__(self, latitude=0.0, longitude=0.0, line1="", line2="", city="",
               state_province="", country="", postal="", elevation="",
               timezone="", properties=defaultdict(list)):
        """ Create a Location object using the given information.
        :param latitude: the decimal degrees north or south of the equator of
            the plant that is its parent. The latitude value is
            a positive (representing northward) or negative (representing
            southward) decimal number in the expected format: ±XX.XXXXXX
            where the digits after the decimal are only necessary when
            expressing increasingly accurate values.
        :param longitude: the decimal degrees east or west from the Prime
            Meridian of the plant that is its parent. The longitude value
            is a positive (representing eastward) or negative (representing
            westward) decimal number in the expected format: ±XXX.XXXXXX
            where the digits after the decimal are necessary when expressing
            increasingly accurate values.
        :param line1:
        :param line2:
        :param city:
        :param state_province:
        :param country:
        :param postal:
        :param elevation:
        :param timezone:
        :param properties:
        :return location: the created Location object
        """

        super(Location, self).__init__(properties)

        self.latitude = str(latitude)
        self.longitude = str(longitude)
        self.line1 = line1
        self.line2 = line2
        self.city = city
        self.stateProvince = state_province
        self.country = country
        self.postal = postal
        self.elevation = elevation
        self.timezone = timezone
        self.properties = properties

    def __str__(self):
        return ''.join(["Location latitude:", self.latitude, ", longitude:",
                        str(self.longitude), ", line1:", str(self.line1),
                        ", line2:", str(self.line2), ", city:", str(self.city),
                        ", stateProvince:", str(self.stateProvince), ", country:",
                        str(self.country)])


class NamePlate(PropertyContainer):
    pass

class DesignElements(PropertyContainer):
    pass

class Array(PropertyContainer):
    def __init__(self, props, array_id=1):
        super(Array, self).__init__(props)
        self.array_id=array_id

class Equipment(PropertyContainer):
    def __init__(self, props, equipment_type='meter'):
        super(Equipment, self).__init__(props)
        self.equipment_type=equipment_type

class Capabilities(PropertyContainer):
    pass

class Participant(PropertyContainer):
    def __init__(self, props, participant_type="owner"):
        super(Participant, self).__init__(props)
        self.participant_type = participant_type


class PlantExtractException(Exception):
    pass


########################
#   command line parsing
if __name__ == '__main__':
    import argparse


    parser = argparse.ArgumentParser(description='Create a Plant Extract Document')
    parser.add_argument('--log', dest='loglevel', default='WARNING',
                        help='set the log level [default:WARNING]')
    parser.add_argument('--test', dest='activate_tests', action='store_true',
                        help='activate doctests for the Plant Extract class')
    # sp = parser.add_subparsers()
    #
    # sp_create = sp.add_parser('create',
    #                           help="Create a plant extract document")

    args = parser.parse_args()
    #   Now for some post parsing output
    # print args.ped

    if args.loglevel is not None:
        loglevel = args.loglevel.upper()
        print ">> Setting loglevel to: " + loglevel
        logger.setLevel(loglevel)

    if args.activate_tests is True:
        """ Run some tests on the PlantExtract class
    >>>   ped = PlantExtract(args.ped[0])
    print ped.last()
    >>>   print 'TmpBOM'
    ps = ped.sunspec_data.get_matching_points('TmpBOM') for p in ps: print
      p.tostring()
    >>>   print 'TotWh'
    ps = ped.sunspec_data.get_matching_points('TotWh') for p in ps: print
    p.tostring() print "Points in period"
    #   start_time: 2012-10-28 22:00:59 end_time: 2012-10-28 22:03:00 > 5 or 6
    #   inclusive
    start_time = dt.datetime(2012, 10, 28, 22, 00, 00)
    end_time = dt.datetime(2012, 10, 28, 22, 03, 00)
    ped.sunspec_data.get_points_in_period(start_time, end_time, 'TotWh')
    """
    else:
        ped = PlantExtract(
            Plant(
                uuid4().urn,
                activation_date="2013-03-02",
                location=Location(latitude=1.1, longitude=2.2,
                                         city="Redwood City",
                                         state_province="CA"),
                name_plate=NamePlate(props=[
                    Property('installedDCCapacity', 'float', '6.5'),
                    Property('installedACCapacity', 'float', '6.4')
                ]),
                design_elements=DesignElements(props=[
                    Property('plantType', 'string', 'commercial')
                ]),
                array=Array(props=[
                    Property('description','string','Carport')
                ], array_id=1),
                equipment=Equipment(props=[
                    Property('Mn', 'string', 'MeterManuf'),
                    Property('Md', 'string', 'MeterModel'),
                    Property('uncertainty', 'float', '0.5')
                ], equipment_type='meter')
            )
        )

        print ped
        print ped.plant
        print ped.plant.location
        print ped.plant.name_plate
        print ped.plant.equipment

        print "JSON PED", ped.toJSON()

        # ped.sunspec_data =

        # print etree.tostring(ped.xml, pretty_print=True)
        # ped = PlantExtract()
        # ped.parse(args.ped[0])
        # print ped
        # print ">> PlantExtract Plant"
        # print ped.plant
        # print ">> PlantExtract parsing sunSpecData"
        # ped.parse_points()
        # print ">> PlantExtract completed parsing of sunSpecData"
        # print ped.sunspec_data  # the sunSpecData block
        # print ped.sunspec_data.device_records[0].models[0].smdx # SMDX info of model
        # print ped.sunspec_data.device_records[0].models[0].points[0] # block structure

