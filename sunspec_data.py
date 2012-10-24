from lxml import etree
from collections import defaultdict
import hashlib, os, logging


smdx_dir    = "smdx"
smdx_prefix = "smdx"
smdx_ext    = ".xml"
smdx_xsd    = "smdx.xsd"

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
        model = SunSpecModel(element, m_id)
        if (model is not None):
          self.models[m_id].append(model)

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
    print '>> Parsing models <<'
    m = self.models
    

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
    
  def parse(self):
    print '>> Parsing only me <<'
    

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
    
    smdx_filename = smdx_prefix + "_" + str.rjust(str(self.model_id), 5, "0") + smdx_ext
    self.exists = False
    smdx = schema = None
    
    try:
      smdx = etree.parse(os.path.join(os.getcwd(), smdx_dir, smdx_filename))
    except IOError:
      logging.warning("IOError caught while opening " + smdx_filename)

    try:
      schema_doc = etree.parse(os.path.join(os.getcwd(), smdx_dir, smdx_xsd))
      schema = etree.XMLSchema(schema_doc)
    except IOError:
      logging.warning("IOError caught while opening " + smdx_xsd)
    
    if (schema is None) or (smdx is None):
      return
    else:
      self.exists = True
      self.__valid(schema, smdx)
  
  def __valid(self, schema, smdx, assert_=False):
    """Determines if this SunSpecModel is valid XML in compliance with the SMDX XSD
    """
    if assert_:
      schema.assert_(smdx)
      self.valid = True
    else:
      self.valid = schema.validate(smdx)
      return self.valid


####################
# Utility functions
def get_attr(element, attr_name):
  attr_value = ''
  if (element is None):
    return attr_value
  elif (element.get(attr_name) is not None):
    attr_value = element.get(attr_name)
  
  return attr_value
