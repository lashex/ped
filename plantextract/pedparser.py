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
from collections import defaultdict
import os
import logging
import datetime as dt

from lxml import etree
from ped import PlantExtract, Plant
from ssparser import SunSpecDataParser

# TODO get these Parser classes flatter and dumping non-Parser objects

xsd_filename = "sunspec_plant_extract.xsd"
xsd_dir = "xsd"
time_format = '%Y-%m-%dT%H:%M:%SZ'
#   logger = logging.getLogger('ped') f =
#   logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s') sh =
#   logging.StreamHandler() sh.setFormatter(f) logger.addHandler(sh)


class PlantExtractParser(object):
    """ A Plant Extract Document processor supporting straightforward
        interaction with information from each of the standard blocks.
    """

    element_name = "sunSpecPlantExtract"

    def __init__(self):
        logging.debug("PlantExtract.__init__()")
        self.xml = None

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

        # check for sunSpecPlantExtract version, assume '2' if absent
        v = env.get('v')
        if v is not None:
            self.version = int(v)
        else:
            self.version = '2'

        # check for sunSpecPlantExtract seqId, assume '1' if absent
        sid = env.get('seqId')
        if sid is not None:
            int(sid)
            self.seqId = sid
        else:
            self.seqId = '1'

        # check for sunSpecPlantExtract lastSeqId, assume '1' if absent
        lid = env.get('lastSeqId')
        if lid is not None:
            int(lid)
            self.lastSeqId = lid
        else:
            self.lastSeqId = '1'

        if int(self.seqId) > int(self.lastSeqId):
            raise PlantExtractException("seqId can't be larger than the lastSeqId")

        self.plant = PlantParser().parse(self.envelope.find(PlantParser.element_name))
        self.sunspec_data = SunSpecDataParser().parse_block(
            self.envelope.find(SunSpecDataParser.element_name)
        )
        # TODO: sunSpecMetadata
        # TODO: strings
        # TODO: extract extensions
        return

    def parse_data(self):
        """Parse the sunSpecData block's Points"""
        if self.sunspec_data.exists and not self.sunspec_data.parsed:
            self.sunspec_data.parse_points()

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

    def objectify(self):
        """ Creates and returns a non-parsing Python representation of the Plant
            Extract Document.
        """
        ped = PlantExtract(self.plant.objectify(), self.seqId, self.lastSeqId)
        ped.time = self.time
        return ped


    # @classmethod
    # def is_ped(cls, ped_file):
    #     """Convenience method to determine if the given file is a Plant Extract
    #     """
    #     is_ped_file = False
    #     try:
    #         ped = PlantExtract()
    #         ped.parse(ped_file)
    #         is_ped_file = True
    #     except PlantExtractException, pexe:
    #         is_ped_file = False
    #         logging.exception("PlantExtract.is_ped() PlantExtractException: %s", pexe)
    #     finally:
    #         return is_ped_file


class PlantParser(object):
    element_name = 'plant'

    def __init__(self):
        logging.debug("Plant.__init__()")

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

        self.location = LocationParser(pe.find(LocationParser.element_name))
        self.name_plate = NamePlateParser(pe.find(NamePlateParser.element_name))
        self.capabilities = CapabilitiesParser(pe.find(CapabilitiesParser.element_name))
        self.participants = list()
        for participant in self.element.iter(Participant.element_name):
            self.participants.append(Participant(participant))

    def tostring(self):
        """Produces a string representation of some parsed Plant values """
        return ''.join(["Plant id:", self.id.hex, ", v:", str(self.version),
                        ", name:", self.name, ", locale:", self.locale,
                        ", description:", self.description])


class PropertyContainerParser(object):
    def __init__(self, my_element):
        self.properties = defaultdict(list)
        self.element = my_element
        if self.element is not None:
            for prop in self.element.iter(PropertyParser.element_name):
                prop_id = prop.get('id')
                prop_type = prop.get('type')
                self.properties[prop_id].append(PropertyParser(prop_id, prop_type,
                                                         prop.text))


class PropertyParser(object):
    element_name = 'property'

    def __init__(self, prop_id, prop_type, text):
        self.id = prop_id
        self.type = prop_type
        self.text = text


class LocationParser(PropertyContainerParser):
    element_name = 'location'

    def __init__(self, location_element):
        super(LocationParser, self).__init__(location_element)

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


class NamePlateParser(PropertyContainerParser):
    element_name = 'namePlate'

    def __init__(self, nameplate_element):
        super(NamePlateParser, self).__init__(nameplate_element)


class CapabilitiesParser(PropertyContainerParser):
    element_name = 'capabilities'

    def __init__(self, capabilities_element):
        super(CapabilitiesParser, self).__init__(capabilities_element)
        print self.properties


class Participant(PropertyContainerParser):
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
        ped = PlantExtractParser()
        ped.parse(args.ped[0])
        print ped
        print ">> PlantExtract Plant"
        print ped.plant
        print ">> PlantExtract parsing sunSpecData"
        ped.parse_data()
        print ">> PlantExtract completed parsing of sunSpecData"
        print ped.sunspec_data  # the sunSpecData block
        print ped.sunspec_data.device_records[0].models[0].smdx # SMDX info of model
        print ped.sunspec_data.device_records[0].models[0].points[0] # block structure

