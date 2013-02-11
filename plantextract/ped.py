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
import os
import logging
import datetime as dt

from lxml import etree
from sunspec_data import SunSpecData


xsd_filename = "sunspec_plant_extract.xsd"
xsd_dir = "xsd"
time_format = '%Y-%m-%dT%H:%M:%SZ'
#   logger = logging.getLogger('ped') f =
#   logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s') sh =
#   logging.StreamHandler() sh.setFormatter(f) logger.addHandler(sh)


class PlantExtract(object):
    """ A Plant Extract Document processor supporting straightforward
        interaction with information from each of the standard blocks.
    """

    element_name = "sunSpecPlantExtract"

    def __init__(self):
        logging.debug("PlantExtract.__init__()")
        self.xml = None

    @classmethod
    def create(cls, plant, ssd=None):
        """Create a plant extract document given parameters and data for the
           standard blocks.
        :param plant: a Plant object with at least a PlantID
        :param ssd: a sunspec_data.DeviceRecord[]
        """
        logging.debug("PlantExtract.create()")

        nowt = dt.datetime.utcnow()

        ped = PlantExtract()

        print plant
        ped.xml = etree.Element(PlantExtract.element_name, seqId="1",
                                lastSeqId="1", t=nowt.strftime(time_format))
        p = etree.SubElement(ped.xml, Plant.element_name,
                             id=str(plant.id.hex), v="1", locale=plant.locale)
        etree.SubElement(p, "name").text = plant.name
        etree.SubElement(p, "description").text = plant.description
        etree.SubElement(p, "notes").text = plant.notes
        if plant.activation_date is not None:
            etree.SubElement(p, "activationDate").text = \
                plant.activation_date.strftime('%Y-%m-%d')
        return ped

    def parse(self, ped_file):
        """Parse the plant extract document (minus sunSpecData)"""
        logging.debug("PlantExtract.parse()")
        # open file and validate
        this_dir, this_filename = os.path.split(__file__)
        xsd_file = os.path.join(this_dir, xsd_dir, xsd_filename)
        self.ped_file = ped_file
        self.tree = etree.parse(self.ped_file)
        schema_doc = etree.parse(xsd_file)
        self.schema = etree.XMLSchema(schema_doc)
        logging.info("PlantExtract.parse() valid_xml:" + str(self.valid_xml()))
        # now parse the Plant Extract
        self.envelope = self.tree.getroot()
        if self.envelope is None:
            raise PlantExtractException("sunSpecPlantExtract root not found.")

        logging.debug("PlantExtract.parse()")
        env = self.envelope
        time = env.get('t')
        if time is None:
            raise PlantExtractException("sunSpecPlantExtract root node 't' attribute is required.")
        else:
            # Plant Extract t="YYYY-MM-DDThh:mm:ssZ"
            self.time = dt.datetime.strptime(time, time_format)

        # check for sunSpecPlantExtract version, assume '1' if absent
        v = env.get('v')
        if v is not None:
            self.version = int(v)
        else:
            self.version = 1

        # check for sunSpecPlantExtract seqId, assume '1' if absent
        sid = env.get('seqId')
        if sid is not None:
            self.seqId = int(sid)
        else:
            self.seqId = 1

        # check for sunSpecPlantExtract lastSeqId, assume '1' if absent
        lid = env.get('lastSeqId')
        if lid is not None:
            self.lastSeqId = int(lid)
        else:
            self.lastSeqId = 1

        if self.seqId > self.lastSeqId:
            raise PlantExtractException("seqId can't be larger than the lastSeqId")

        self.plant = Plant().parse(self.envelope.find(Plant.element_name))
        self.sunspec_data = SunSpecData().parse_block(self.envelope.find(SunSpecData.element_name))
        # TODO: sunSpecMetadata
        # TODO: strings
        # TODO: extract extensions
        return

    def parse_data(self):
        """Parse the sunSpecData block"""
        if self.sunspec_data.exists and not self.sunspec_data.parsed:
            self.sunspec_data.parse_data()

    def __str__(self):
        """Produces a string representation of the Plant Extract envelope"""
        return ''.join(['PlantExtract v:', str(self.version), ' t:', str(self.time),
                        ' seqId:', str(self.seqId), ' lastSeqId:', str(self.lastSeqId)])

    def last(self):
        """Determines if this Plant Extract is the last extract in a set
        """
        return self.seqId == self.lastSeqId

    def valid_xml(self, assert_=False):
        """Determines if this Plant Extract is valid XML in compliance with the XSD"""
        if assert_:
            self.schema.assert_(self.tree)
            self.valid = True
        else:
            self.valid = self.schema.validate(self.tree)

        return self.valid

    @classmethod
    def is_ped(cls, ped_file):
        """Convenience method to determine if the given file is a Plant Extract
        """
        is_ped_file = False
        try:
            ped = PlantExtract()
            ped.parse(ped_file)
            is_ped_file = True
        except PlantExtractException, pexe:
            is_ped_file = False
            logging.exception("PlantExtract.is_ped() PlantExtractException: %s", pexe)
        finally:
            return is_ped_file


class Plant(object):
    element_name = 'plant'

    def __init__(self):
        logging.debug("Plant.__init__()")

    @classmethod
    def create(cls, plant_id, locale="en-US", name="", notes="",
               description="", activation_date=None, location=None):
        """

        :param plant_id:
        :param locale:
        :param name:
        :param notes:
        :param description:
        :param activation_date: the date the power plant was actively
            delivering power to the utility grid or energy off-taker. The
            activation_date value must be compliant with the ISO 8601 date
            format: "YYYY-MM-DD”
        :param location:
        :return:
        """
        plant = Plant()
        plant.id = plant_id
        plant.locale = locale
        plant.name = name
        plant.notes = notes
        plant.description = description
        if activation_date is not None:
            plant.activation_date = dt.datetime.strptime(activation_date,
                                                         '%Y-%m-%d')
        plant.location=location
        return plant

    def parse(self, element):
        self.element = pe = element
        if pe is None:
            raise PlantExtractException("plant element not found")

        plant_id = pe.get('id')
        if plant_id is None:
            raise PlantExtractException("plant 'id' attribute is required.")
        else:
            self.id = UUID(plant_id)

        v = pe.get('v')
        if v is not None:
            self.version = int(v)

        self.locale = pe.get('locale')
        self.name = get_node_value(pe, 'name')
        self.description = get_node_value(pe, 'description')
        self.notes = get_node_value(pe, 'notes')
        ad = get_node_value(pe, 'activationDate')
        if ad is not None:
            self.activation_date = dt.datetime.strptime(ad, '%Y-%m-%d')

        self.location = Location(pe.find(Location.element_name))
        self.name_plate = NamePlate(pe.find(NamePlate.element_name))
        self.capabilities = Capabilities(pe.find(Capabilities.element_name))
        self.participants = list()
        for participant in self.element.iter(Participant.element_name):
            self.participants.append(Participant(participant))

    def tostring(self):
        """Produces a string representation of some parsed Plant values """
        return ''.join(["Plant id:", self.id.hex, ", v:", str(self.version),
                        ", name:", self.name, ", locale:", self.locale,
                        ", description:", self.description])


class PropertyContainer(object):
    def __init__(self, my_element):
        self.properties = defaultdict(list)
        self.element = my_element
        if self.element is not None:
            for prop in self.element.iter(Property.element_name):
                prop_id = prop.get('id')
                prop_type = prop.get('type')
                self.properties[prop_id].append(Property(prop_id, prop_type,
                                                         prop.text))


class Property(object):
    element_name = 'property'

    def __init__(self, prop_id, prop_type, text):
        self.id = prop_id
        self.type = prop_type
        self.text = text


class Location(PropertyContainer):
    element_name = 'location'

    def __init__(self, location_element):
        super(Location, self).__init__(location_element)

    @classmethod
    def create(cls, latitude=0.0, longitude=0.0, line1="", line2="", city="",
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
        loc = Location(None)
        loc.latitude = str(latitude)
        loc.longitude = str(longitude)
        loc.line1 = line1
        loc.line2 = line2
        loc.city = city
        loc.stateProvince = state_province
        loc.country = country
        loc.postal = postal
        loc.elevation = elevation
        loc.timezone = timezone
        loc.properties = properties
        return loc

    def parse(self):
        le = self.element
        self.latitude = get_node_value(le, 'latitude')
        self.longitude = get_node_value(le, 'longitude')
        self.line1 = get_node_value(le, 'line1')
        self.line2 = get_node_value(le, 'line2')
        self.city = get_node_value(le, 'city')
        self.stateProvince = get_node_value(le, 'stateProvince')
        self.country = get_node_value(le, 'country')
        self.postal = get_node_value(le, 'postal')
        self.elevation = get_node_value(le, 'elevation')
        self.timezone = get_node_value(le, 'timezone')


class NamePlate(PropertyContainer):
    element_name = 'namePlate'

    def __init__(self, nameplate_element):
        super(NamePlate, self).__init__(nameplate_element)


class Capabilities(PropertyContainer):
    element_name = 'capabilities'

    def __init__(self, capabilities_element):
        super(Capabilities, self).__init__(capabilities_element)
        print self.properties


class Participant(PropertyContainer):
    element_name = 'participant'

    def __init__(self, participant_element):
        super(Participant, self).__init__(participant_element)
        self.type = get_node_value(self.element, 'type')


class PlantExtractException(Exception):
    pass


#####################
#   Utility functions
def get_node_value(node, node_name):
    node_value = None

    if node is None:
        return None
    elif node.find(node_name) is not None:
        node_value = node.find(node_name).text

    return node_value

########################
#   command line parsing
if __name__ == '__main__':
    import argparse


    parser = argparse.ArgumentParser(description='Process or create Plant Extract Documents')
    parser.add_argument('--log', dest='loglevel', default='WARNING',
                        help='set the log level (default:WARNING)')
    parser.add_argument('--test', dest='activate_tests', action='store_true',
                        help='activate doctests for the Plant Extract class')
    sp = parser.add_subparsers()

    sp_create = sp.add_parser('create',
                              help="Create a plant extract document")

    sp_parse = sp.add_parser('parse', help="Parse a plant extract document")
    sp_parse.add_argument('--ped', type=file, nargs='+',
                          help='one or more plant extract documents to process - absolute path')
    sp_parse.add_argument('--xsd', type=file, nargs=1,
                          help='override the default XML schema document for validation')
    sp_parse.add_argument('--novalid', dest='validation', action='store_false',
                          help='do not validate the given plant extract documents')

    args = parser.parse_args()
    #   Now for some post parsing output
    # print args.ped

    if args.loglevel is not None:
        loglevel = args.loglevel.upper()
        print ">> Setting loglevel to: " + loglevel
        logging.getLogger().setLevel(loglevel)

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
        # xsd_full_file = os.path.join(os.getcwd(), xsd_dir, xsd_filename)
        ped = PlantExtract.create(
            Plant.create(
                uuid4(),
                activation_date="2012-12-02",
                location=Location.create(latitude=1.1, longitude=2.2,
                                         city="Redwood City",
                                         state_province="CA")
            ),
        )
        print etree.tostring(ped.xml, pretty_print=True)
        # ped = PlantExtract()
        # ped.parse(args.ped[0])
        # print ped
        # print ">> PlantExtract Plant"
        # print ped.plant
        # print ">> PlantExtract parsing sunSpecData"
        # ped.parse_data()
        # print ">> PlantExtract completed parsing of sunSpecData"
        # print ped.sunspec_data  # the sunSpecData block
        # print ped.sunspec_data.device_records[0].models[0].smdx # SMDX info of model
        # print ped.sunspec_data.device_records[0].models[0].points[0] # block structure

