from lxml import etree
from lxml import objectify
from collections import defaultdict
from sunspec_smdx import SMDX, SMDXPoint
import hashlib, os, logging



class SunSpecData(object):
  
  def __init__(self, data_element):
    """Initialize a SunSpecData object given the XML Element
    """
    self.data_element = data_element
    if self.data_element is None: 
      self.exists = False
      return
    else: self.exists = True
    
    # check for sunSpecData version, assume '1' if absent
    v = self.data_element.get('v')
    if (v is not None): self.version = int(v)
    else: self.version = 1
    
    self.device_records = list()
    for d_record in self.data_element.iter(DeviceRecord.element_name):
      self.device_records.append(DeviceRecord(d_record))

  def parse(self):
    logging.info("SunSpecData.parse()")
    for dr in self.device_records:
      dr.parse()

  def tostring(self):
    s = "SunSpecData v:" + str(self.version)
    s += "xml: " + etree.tostring(self.data_element, pretty_print=True)
    
    return s


class DeviceRecord(object):
  element_name = 'd'

  def __init__(self, element):
    element = element
    if element is None:
      print "DeviceRecord element provided is None"
      return

    self.manufacturer = get_attr(element, 'man')
    self.model = get_attr(element, 'mod')
    self.serial_number = get_attr(element, 'sn')
    self.logger_id = get_attr(element, 'lid')
    self.logger_id_namespace = get_attr(element, 'ns')
    self.device_interface_id = get_attr(element, 'if')
    self.device_id = get_attr(element, 'id')
    self.correlation_id = get_attr(element, 'cid')

    self.__determine_id()
    print self.tostring()

    self.models = defaultdict(list)
    for m in element.iter('m'):
        m_id = m.get('id')
        if (m_id is not None):
          logging.info("DeviceRecord.__init__() appending model_id: " + m_id)
          self.models[m_id].append(SunSpecModel(element, m_id))

  def __determine_id(self):
    self.device_id_type = None
    gs = None
    if (len(self.model) > 0 and len(self.manufacturer) > 0 and len(self.serial_number) > 0):
      gs = "" + self.serial_number + self.model + self.manufacturer
      self.device_id_type = 'Common Block'
    elif (len(self.logger_id) > 0 and len(self.device_id) > 0):
      gs = "" + self.device_id + self.logger_id
      self.device_id_type = 'Logger-specific, user-assigned'

    if gs is None:
      s = "A Device must have a globally unique identifier, either man: mod: sn: or lid: id:"
      raise SunSpecDataException(s)
    
    self.guid = int(hashlib.md5(gs).hexdigest(), 16)
    return
    
  def parse(self):
    logging.info("SunSpecData.DeviceRecord.parse()")
    m = self.models
    print m

  def tostring(self):
    s  = "Device" + os.linesep
    s += " id_type:'" + self.device_id_type + "' guid:" + str(self.guid) + os.linesep
    s += " man:" + self.manufacturer + " mod:" + self.model + " sn:" + self.serial_number + os.linesep
    s += " lid:" + self.logger_id + " ns:" + self.logger_id_namespace 
    s += " id:"  + self.device_id + os.linesep
    s += " if:"  + self.device_interface_id + " cid:" + self.correlation_id
    
    return s


class Model(object):
  
  def __init__(self, element, model_id):
    self.points = defaultdict(list)
    if (element is None):
      raise SunSpecDataException("SunSpec model element is required for a Model")
    else:
      self.element = element
    
    if (model_id is None):
      raise SunSpecDataException("SunSpec model element must have an id attribute")
    else:
      self.model_id = int(model_id)

    print '>> contsructing model for model_id:' + str(model_id)
    

class Point(object):

  def __init__(self, element):
    element = element


class SunSpecDataException(Exception):
  
  def __init__(self, argument):
    super(SunSpecDataException, self).__init__(argument)
    self.argument = argument


class SunSpecModel(Model):

  def __init__(self, element, model_id=None):
    super(SunSpecModel, self).__init__(element, model_id)

    smdx = SMDX(element, model_id)
    print smdx.get_points()


####################
# Utility functions
def get_attr(element, attr_name):
  attr_value = ''
  if (element is None):
    return attr_value
  elif (element.get(attr_name) is not None):
    attr_value = element.get(attr_name)
  
  return attr_value
