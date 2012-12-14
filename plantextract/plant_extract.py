from uuid import UUID
from collections import defaultdict
import os
import logging
import datetime as dt

from lxml import etree

from sunspec_data import SunSpecData
from ts_calc import TimeSeriesCalc, ts_SUM


xsd_filename = "sunspec_plant_extract.xsd"
xsd_dir = "xsd"
#   logger = logging.getLogger('ped') f =
#   logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s') sh =
#   logging.StreamHandler() sh.setFormatter(f) logger.addHandler(sh)


class PlantExtract(object):
    ''' Process a Plant Extract Document and allow straightforward retrieval of information
        from each of the standard blocks.
    '''

    def __init__(self, ped_file, xsd_file):
        logging.debug("PlantExtract.__init__()")
        # open file and validate
        self.ped_file = ped_file
        self.tree = etree.parse(self.ped_file)
        schema_doc = etree.parse(xsd_file)
        self.schema = etree.XMLSchema(schema_doc)
        valid = self.valid(True)  # TODO: interpret command line 'validate' arg
        logging.info("PlantExtract.__init__() valid:" + str(valid))
        # now parse the Plant Extract
        self.envelope = self.tree.getroot()
        if self.envelope is None:
            raise PlantExtractException("sunSpecPlantExtract root not found.")

        self._parse()

    def _parse(self):
        """Parse the plant extract document (minus sunSpecData)"""
        logging.debug("PlantExtract._parse()")
        env = self.envelope
        time = env.get('t')
        if time is None:
            raise PlantExtractException("sunSpecPlantExtract root node 't' attribute is required.")
        else:
            # Plant Extract t="YYYY-MM-DDThh:mm:ssZ"
            self.time = dt.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')

    #   check for sunSpecPlantExtract version, assume '1' if absent
        v = env.get('v')
        if v is not None:
            self.version = int(v)
        else:
            self.version = 1

    #   check for sunSpecPlantExtract seqId, assume '1' if absent
        sid = env.get('seqId')
        if sid is not None:
            self.seqId = int(sid)
        else:
            self.seqId = 1

    #   check for sunSpecPlantExtract lastSeqId, assume '1' if absent
        lid = env.get('lastSeqId')
        if lid is not None:
            self.lastSeqId = int(lid)
        else:
            self.lastSeqId = 1

        if self.seqId > self.lastSeqId:
            raise PlantExtractException("seqId can't be larger than the lastSeqId")

        self.plant = Plant(self.envelope.find(Plant.element_name))
        self.sunspec_data = SunSpecData(self.envelope.find(SunSpecData.element_name))
    #   TODO: sunSpecMetadata TODO: strings TODO: extract extensions
        return

    def parse_data(self):
        if self.sunspec_data.exists and not self.sunspec_data.parsed:
            self.sunspec_data.parse()

    def tostring(self):
        """Produces a string representation of the Plant Extract standard blocks """
        return ''.join(['PlantExtract v:', str(self.version), ' t:', str(self.time),
                        ' seqId:', str(self.seqId), ' lastSeqId:', str(self.lastSeqId)])

    def last(self):
        """Determines if this Plant Extract is the last extract in a set
        """
        return self.seqId == self.lastSeqId

    def valid(self, assert_=False):
        """Determines if this Plant Extract is valid XML in compliance with the XSD"""
        if assert_:
            self.schema.assert_(self.tree)
            self.valid = True
        else:
            self.valid = self.schema.validate(self.tree)

        return self.valid


class Plant(object):
    element_name = 'plant'

    def __init__(self, element):
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
                        ", name:", self.name])


class PropertyContainer(object):

    def __init__(self, my_element):
        self.properties = defaultdict(list)
        self.element = my_element
        if self.element is not None:
            for property in self.element.iter(Property.element_name):
                prop_id = property.get('id')
                prop_type = property.get('type')
                self.properties[prop_id].append(Property(prop_id, prop_type,
                                                         property.text))


class Property(object):
    element_name = 'property'

    def __init__(self, id, type, text):
        self.id = id
        self.type = type
        self.text = text


class Location(PropertyContainer):
    element_name = 'location'

    def __init__(self, location_element):
        super(Location, self).__init__(location_element)

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

    def __init__(self, argument):
        super(PlantExtractException, self).__init__(argument)
        self.argument = argument


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
    cmd_parser = argparse.ArgumentParser(description='Process one or more Plant Extract Documents')
    cmd_parser.add_argument('ped', type=file, nargs='+',
                            help='one or more plant extract documents to process - absolute path')
    cmd_parser.add_argument('--xsd', type=file, nargs=1,
                            help='override the default XML schema document for validation')
    cmd_parser.add_argument('--novalid', dest='validation', action='store_false',
                            help='do not validate the given plant extract documents')
    cmd_parser.add_argument('--log', dest='loglevel', default='WARNING',
                            help='set the log level (default:WARNING)')
    cmd_parser.add_argument('--test', dest='activate_tests', action='store_true',
                            help='activate doctests for the Plant Extract class')

    args = cmd_parser.parse_args()
    #   Now for some post parsing output
    print args.ped

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
        xsd_full_file = os.path.join(os.getcwd(), xsd_dir, xsd_filename)
        ped = PlantExtract(args.ped[0], xsd_full_file)
        print ped.tostring()
        print ">> PlantExtract Plant"
        print ped.plant.tostring()
        print ">> PlantExtract parsing sunSpecData"
        ped.parse_data()
        print ped.sunspec_data.tostring()
        print ">> PlantExtract completed parsing of sunSpecData"
        tsc = TimeSeriesCalc(ped)
        print tsc.energy()
        print tsc.energy_exported()
