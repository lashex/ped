from lxml import etree
from lxml import objectify
from collections import defaultdict
from sunspec_smdx import SMDX, SMDXPoint
import datetime
import hashlib, os, logging

# logger = logging.getLogger('ped.ssd')


class SunSpecData(object):
  element_name = 'sunSpecData'
  
  def __init__(self, element):
    '''Initialize a SunSpecData object given the XML Element
    '''
    self.element = element
    if self.element is None: 
      self.exists = False
      return
    else: self.exists = True
    
    # check for sunSpecData version, assume '1' if absent
    v = self.element.get('v')
    if (v is not None): self.version = int(v)
    else: self.version = 1
    
    self.device_records = list()
    for d_record in self.element.iter(DeviceRecord.element_name):
      self.device_records.append(DeviceRecord(d_record))

  def parse(self):
    logging.debug("SunSpecData.parse()")
    for dr in self.device_records:
      dr.parse()
    self.get_points_in_period(None, None)

  def tostring(self):
    s = "SunSpecData v:" + str(self.version)
    s += "xml: " + etree.tostring(self.element, pretty_print=True)
    
    return s
    
  def get_matching_points(self, point_id):
    '''Get a list of points which match the given point_id
    '''
    points = list()
    logging.debug("SunSpecData.get_matching_points() looking for point_id:"+str(point_id))
    for dr in self.device_records:
      models = dr.models
      if models is not None:
        for m in models:
          plist = m.get_matching_points(point_id)
          if (plist is not None) and (len(plist) > 0):
            points.append(plist)
    
    return points
    
  def get_points_in_period(self, startTime, endTime):
    now = datetime.datetime.now()
    if startTime is None:
      startTime =  now - datetime.timedelta(minutes=15)
    if endTime is None:
      endTime = now
    
    all_points = list()
    for dr in self.device_records:
      for model in dr.models:
        print model.points
        all_points = all_points + model.points

    for p in all_points:
      print p.tostring()
    return



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

    self._determine_id()
    time = get_attr(element, 't')
    if (time is None) or (time is ''):
      raise SunSpecDataException("DeviceRecord 't' attribute is required.")
    else:
      # SunSpecData <d ... t="YYYY-MM-DDThh:mm:ssZ"
      self.time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')

    self.models = list()
    for m in element.iter(Model.element_name):
        m_id = m.get('id')
        if (m_id is not None):
          logging.info("DeviceRecord.__init__() adding model_id: " + m_id)
          self.models.append(Model(m, m_id, self.time))

  def _determine_id(self):
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
    for model in self.models:
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
  element_name = 'm'
  
  def __init__(self, element, id, dr_time):
    self.dr_time = dr_time
    self.points = list()
    if (element is None):
      raise SunSpecDataException("SunSpec model element is required for a Model")
    else:
      self.element = element
    
    if (id is None):
      raise SunSpecDataException("SunSpec model element must have an id attribute")
    else:
      self.id = int(id)

    self.smdx = SMDX(element, id)
    logging.info('Model constructed for model_id:' + str(id))


  def parse(self):
    logging.debug("Model.parse() model_id:" + str(self.id))

    logging.info("Model.parse() instantiating Points")
    for p in self.element.iter(Point.element_name):
      self.points.append(Point(self, p))
    
    smdx_points = self.smdx.get_points()
    logging.info("Model.parse() adding units from SMDXPoints to Points")
    for p in self.points:
      if p.id in smdx_points:
        logging.info("Point.id:" + str(p.id) + " found in SMDX.model_id: " + str(self.id))
        p.unit = smdx_points[p.id].units
      else:
        logging.warning("Point.id:"+ str(p.id) + 
                        " exists but shouldn't for SMDX.model_id: " + str(self.id))

    mand_met = False
    if (len(self._has_mandatory_points()) == 0):
      mand_met = True
    logging.debug("Model.parse() has all mandatory points? " + str(mand_met))
  
  
  def get_matching_points(self, point_id):
    '''Get a list of points which match the given point_id
    '''
    points = list() 
    logging.info("Model.get_matching_points() looking for point_id:"+str(point_id))
    for p in self.points:
      logging.debug("Model.get_matching_points() p.id:"+p.id +" given point_id:"+point_id)
      if p.id == point_id:
        points.append(p)
    
    return points


  def _has_mandatory_points(self):
    man_points = self.smdx.get_mandatory_points()
    points = self.points
    logging.debug("Model._has_mandatory_points()")
    missing_mand = {}
    
    for sp in man_points.itervalues():
      if sp.mandatory:
        found = False
        for p in points:
          if sp.id == p.id:
            print "Found mandatory point", p.id
            found = True
            break

        if not found:
          logging.warning("Model.id:" + str(self.id) + 
                          " missing mandatory SMDXPoint.id:" + sp.id)
          missing_mand[sp.id] = sp
    
    return missing_mand

  def set_metadata(self, element):
    
    return
    
  def tostring(self):
    return ''.join(['Model.id:', str(self.id), ' dr_time:', str(self.dr_time)])


class Point(object):
  element_name = 'p'

  def __init__(self, model, element):
    self.model = model
    element = element
    self.id    = element.get('id')
    self.x     = element.get('x')
    self.text  = element.text
    self.units = None

    time = element.get('t')
    if time is None:
      self.time = model.dr_time
    else:
      # SunSpecData <p ... t="YYYY-MM-DDThh:mm:ssZ"
      self.time = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')

  def tostring(self):
    return ''.join(['Point.id:', self.id, ' x:', str(self.x), ' text:', str(self.text), 
                    ' units:', str(self.units), ' t:', str(self.time)])

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
