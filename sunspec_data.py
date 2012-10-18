from lxml import etree
import hashlib, os


class SunSpecData(object):
  
  def __init__(self, data_element):
    """Initialize a SunSpecData object given the XML Element
    """
    self.data_element = data_element
    if self.data_element is None: return
    
    # check for sunSpecData version, assume '1' if absent
    v = self.data_element.get('v')
    if (v is not None): self.version = int(v)
    else: self.version = 1
    
  def parse(self):
    self.device_records = list()
    for d_record in self.data_element.iter(DeviceRecord.element_name):
      self.device_records.append(DeviceRecord(d_record))


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

    self.models = list()

  def __determine_id(self):
    self.device_id_type = None
    gs = None
    if (len(self.model) > 0 and len(self.manufacturer) > 0 and len(self.serial_number) > 0):
      gs = "" + self.serial_number + self.model + self.manufacturer
      self.device_id_type = 'Common Block'
    elif (len(self.logger_id) > 0 and len(self.device_id) > 0):
      gs = "" + self.device_id + self.logger_id
      self.device_id_type = 'Logger-specific, user-assigned'

    self.guid = int(hashlib.md5(gs).hexdigest(), 16)
    return

  def tostring(self):
    s  = "Device" + os.linesep
    s += " id_type:'" + self.device_id_type + "' guid:" + str(self.guid) + os.linesep
    s += " man:" + self.manufacturer + " mod:" + self.model + " sn:" + self.serial_number + os.linesep
    s += " lid:" + self.logger_id + " ns:" + self.logger_id_namespace 
    s += " id:"  + self.device_id + os.linesep
    s += " if:"  + self.device_interface_id + " cid:" + self.correlation_id
    return s


class Model(object):
  
  def __init__(self, element):
    self.points = list()
    element = element
    
class Point(object):

  def __init__(self, element):
    element = element


####################
# Utility functions
def get_attr(element, attr_name):
  attr_value = ''
  if (element is None):
    return attr_value
  elif (element.get(attr_name) is not None):
    attr_value = element.get(attr_name)
  
  return attr_value