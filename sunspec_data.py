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
    logging.debug("SunSpecData.parse()")
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

    self.__determine_id()

    self.models = {}
    for m in element.iter('m'):
        m_id = m.get('id')
        if (m_id is not None):
          logging.info("DeviceRecord.__init__() adding model_id: " + m_id)
          self.models[m_id] = Model(m, m_id)

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
    logging.debug("SunSpecData.DeviceRecord.parse()")
    for m_id, model in self.models.items():
      model.parse()

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
    self.points = {}
    if (element is None):
      raise SunSpecDataException("SunSpec model element is required for a Model")
    else:
      self.element = element
    
    if (model_id is None):
      raise SunSpecDataException("SunSpec model element must have an id attribute")
    else:
      self.model_id = int(model_id)

    self.smdx = SMDX(element, model_id)
    logging.info('Model constructed for model_id:' + str(model_id))


  def parse(self):
    logging.debug("Model.parse() model_id:" + str(self.model_id))
    self.points = self.get_points()
    self.__has_mandatory_points()
  
  
  def get_points(self):
    logging.info("Model.get_points() instantiating Points")
    for p in self.element.iter('p'):
      point = Point(p)
      self.points[point.id] = point
    
    smdx_points = self.smdx.get_points()
    logging.info("Model.get_points() adding units from SMDXPoints to Points")
    for p_id, p in self.points.items():
      if p.id in smdx_points:
        p.unit = smdx_points[p.id].units
      else:
        logging.warning("Point.id:"+ str(p.id) + 
                        " exists in Model but shouldn't for model_id: " + 
                        str(self.model_id))
      
    return self.points


  def __has_mandatory_points(self):
    man_points = self.smdx.get_mandatory_points()
    points = self.points
    logging.debug("Model.__has_mandatory_points()")
    missing_mand = {}
    
    for sp_id, sp in man_points.items():
      if sp.mandatory:
        if sp.id in points:
          continue
        else:
          logging.warning("Model.model_id:" + str(self.model_id) + 
                          " missing mandatory point with id:" + sp.id)
          missing_mand[sp.id] = sp
    
    return missing_mand


class Point(object):

  def __init__(self, element):
    element = element
    self.id    = element.get('id')
    self.x     = element.get('x')
    self.text  = element.text
    self.units = None


class SunSpecDataException(Exception):
  
  def __init__(self, argument):
    super(SunSpecDataException, self).__init__(argument)
    self.argument = argument



####################
# Utility functions
def get_attr(element, attr_name):
  attr_value = ''
  if (element is None):
    return attr_value
  elif (element.get(attr_name) is not None):
    attr_value = element.get(attr_name)
  
  return attr_value
