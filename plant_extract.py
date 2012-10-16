from lxml import etree
from xml.etree.ElementTree import Element
from datetime import datetime
from uuid import UUID
from collections import defaultdict
import argparse, os


xsd_filename = "sunspec_plant_extract.xsd"
xsd_dir = "xml"

class PlantExtract(object):

  def __init__(self, ped_filename):
    # open file, parse and validate
    self.ped_filename = ped_filename
    self.tree = etree.parse(self.ped_filename)
    schema_doc = etree.parse(os.path.join(os.getcwd(), xsd_dir, xsd_filename))
    self.schema = etree.XMLSchema(schema_doc)
    self.valid()
    
    # now parse the Plant Extract
    self.envelope = self.tree.getroot()
    if self.envelope is None:
      raise PlantExtractException("sunSpecPlantExtract root node not found.")
    self.__parse()
    
  def tostring(self):
    """Produces a string representation of the entire Plant Extract XML tree
    """
    return etree.tostring(self.tree, pretty_print=True)

  def __parse(self):
    env = self.envelope
    time = env.get('t')
    if time is None:
      raise PlantExtractException("sunSpecPlantExtract root node 't' attribute is required.")
    else:
      # Plant Extract t="YYYY-MM-DDThh:mm:ssZ"
      self.time = datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')
      
    self.version = int(env.get('v'))
    self.seqId = int(env.get('seqId'))
    self.lastSeqId = int(env.get('lastSeqId'))
    if self.seqId > self.lastSeqId:
      raise PlantExtractException("seqId can't be larger than the lastSeqId")
    
    self.plant = Plant(self.envelope.find('plant'))
    # TODO: sunSpecData 
    # TODO: sunSpecMetadata
    # TODO: strings
    # TODO: extract extensions
    return

  def last(self):
    """Determines if this Plant Extract is the last extract in a set
    """
    if self.seqId == self.lastSeqId:
      return True
    else:
      return False
      
  def valid(self, assert_=False):
    """Determines if this Plant Extract is valid XML in compliance with the XSD
    """
    if assert_:
      self.schema.assert_(self.tree)
    else:
      return self.schema.validate(self.tree)


class Plant(object):
  
  def __init__(self, plant_element):
    self.plant_element = pe = plant_element
    plant_id = pe.get('id')
    if plant_id is None:
      raise PlantExtractException("plant 'id' attribute is required.")
    else:
      self.id = UUID(plant_id)
    
    self.version = pe.get('v')
    self.locale = pe.get('locale')
    self.name = pe.find('name').text
    self.description = pe.find('description').text
    self.notes = pe.find('notes').text
    ad = pe.find('activationDate').text
    self.activation_date = datetime.strptime(ad, '%Y-%m-%d')
    self.location = Location(pe.find(Location.element_name))
    self.name_plate = NamePlate(pe.find(NamePlate.element_name))
    self.capabilities = Capabilities(pe.find(Capabilities.element_name))
    
    self.participants = list()
    for participant in self.plant_element.iter(Participant.element_name):
    	self.participants.append(Participant(participant))
		  
  def tostring(self):
    """Produces a string representation of key parsed Plant values
    """
    s = ("Plant id:" + self.id.hex + ", v:" + self.version + ", name:"  + self.name +
         ", activation:" + self.activation_date.isoformat())
    return s


class PropertyContainer(object):
  
  def __init__(self, my_element):
    self.properties = defaultdict(list)
    self.element = my_element
    for property in self.element.iter('property'):
      prop_id = property.get('id')
      prop_type = property.get('type')
      self.properties[prop_id].append(Property(prop_id, prop_type, property.text))


class Property(object):

  def __init__(self, id, type, text):
    self.id = id
    self.type = type
    self.text = text


class Location(PropertyContainer):
  element_name = str('location')
  
  def __init__(self, location_element):
    super(Location, self).__init__(location_element)
    le = self.element
    self.latitude = float(le.find('latitude').text)
    self.longitude = float(le.find('longitude').text)
    # TODO: flesh out more location values


class NamePlate(PropertyContainer):
	element_name = str('namePlate')
	
	def __init__(self, nameplate_element):
		super(NamePlate, self).__init__(nameplate_element)


class Capabilities(PropertyContainer):
	element_name = str('capabilities')
	
	def __init__(self, capabilities_element):
		super(Capabilities, self).__init__(capabilities_element)
		print self.properties


class Participant(PropertyContainer):
	element_name = str('participant')
	
	def __init__(self, participant_element):
		super(Participant, self).__init__(participant_element)
		self.type = self.element.get('type')


class PlantExtractException(Exception):
  
  def __init__(self, argument):
    self.argument = argument


# command line parsing
cmd_parser = argparse.ArgumentParser(description='Process one or more Plant Extract Documents')
cmd_parser.add_argument('ped', type=file, nargs='+',
                        help='one or more plant extract documents to process - absolute path')
cmd_parser.add_argument('--xsd', type=file, nargs=1, 
                        help='override the default XML schema document for validation')
cmd_parser.add_argument('--novalid', dest='validation', action='store_false',
                        help='do not validate the given plant extract documents')

args = cmd_parser.parse_args()

# Now for some post parsing output
print args.ped

ped = PlantExtract(args.ped[0])
print ped.tostring()
print 't:'+ped.time.isoformat()+' v'+str(ped.version)+' '+str(ped.seqId)+':'+str(ped.lastSeqId)
print ped.last()
print ped.valid()
print ped.plant.tostring()