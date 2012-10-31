from lxml import etree
from lxml import objectify
from collections import defaultdict
import hashlib, os, logging


smdx_dir    = "smdx"
smdx_prefix = "smdx"
smdx_ext    = ".xml"
smdx_xsd    = "smdx.xsd"
smdx_schema_parser = None



class SMDX(object):
  def __init__(self, element, model_id):
    self.exists = False
    self.smdx_tree = None
    self.model_id = model_id
    smdx_filename = smdx_prefix + "_" + str.rjust(str(self.model_id), 5, "0") + smdx_ext

    parser = get_smdx_parser()
    
    try:
      self.smdx_tree = objectify.parse(os.path.join(os.getcwd(), smdx_dir, smdx_filename), 
                                       parser)
    except IOError:
      logging.warning("IOError caught while opening " + smdx_filename)
      
    if (self.smdx_tree is None):
      return
    else:
      self.exists = True
    
    
  def get_points(self):
    root = self.smdx_tree.getroot()
    points = defaultdict(list)
    for p in root.model.block.point:
      p_id = p.get('id')
      points[p_id].append(SMDXPoint(p))
    
    return points

class SMDXPoint(object):
  '''SMDX Point class that understands points like:
    <point id="PhVphA" offset="8" type="uint16" sf="V_SF" units="V" mandatory="true" />
  '''
  def __init__(self, element):
    element = element
    if (element is None) or (element.tag != 'point'):
      logging.info("SMDXPoint objects must have a point element")
      return
    
    self.id     = element.get('id')
    self.len    = element.get('len')
    self.offset = element.get('offset')
    self.type   = element.get('type')
    self.sf     = element.get('sf')
    self.units  = element.get('units')
    self.access = element.get('access')
    self.mandatory = bool(element.get('mandatory'))
    

def get_smdx_parser():
  global smdx_schema_parser
  if (smdx_schema_parser is None):
    try:
      schema_etree = etree.parse(os.path.join(os.getcwd(), smdx_dir, smdx_xsd))
      schema = etree.XMLSchema(schema_etree)
      schema_parser = objectify.makeparser(schema = schema)
      logging.info("get_smdx_parser() getting a global lxml.objectify SMDX parser")
    except IOError:
      logging.warning("IOError caught while opening " + schema_filename)

  return smdx_schema_parser
    


#     try:
#       smdx_etree = etree.parse(os.path.join(os.getcwd(), smdx_dir, smdx_filename))
#     except IOError:
#       logging.warning("IOError caught while opening " + smdx_filename)
# 
#     try:
#       schema_etree = etree.parse(os.path.join(os.getcwd(), smdx_dir, smdx_xsd))
#       schema = etree.XMLSchema(schema_etree)
#     except IOError:
#       logging.warning("IOError caught while opening " + smdx_xsd)
#     
#     if (schema_etree is None) or (smdx_etree is None):
#       return
#     else:
#       self.exists = True
#       self.__valid(schema, smdx_etree)
#       
#     smdx = SMDX(smdx_etree.getroot())
# 
# 
#   def __valid(self, schema, smdx, assert_=False):
#     """Determines if this SunSpecModel is valid XML in compliance with the SMDX XSD
#     """
#     if assert_:
#       schema.assert_(smdx)
#       self.valid = True
#     else:
#       self.valid = schema.validate(smdx)
#       return self.valid
#       
#   def parse(self):
#     
#     return
# 
# class SMDX(object):
#   def __init__(self, root):
#     self.root = root
#     self.exists = False
#     if self.root is None: return
#     else:
#       self.exists = True
#       self.__parse()
#       return
#   
#   def __parse(self):
#     """Parse the SMDX document
#     """
#     l = self.root.xpath('strings/model/label')
#     self.label = l[0].text
#     
#     self.points = defaultdict(list)
#     point_elements = self.root.xpath('model//point')
#     for p in point_elements:
#       p_id = p.get('id')
#       self.points[p_id].append(SMDXPoint(p))
#       
# 
# class SMDXPoint(object):
#   def __init__(self, element):
#     e = element
#     # check for sunSpecPlantExtract seqId, assume '1' if absent
#     self.id     = e.get('id')
#     self.offset = e.get('offset')
#     self.type   = e.get('type')
#     self.sf = e.get
# 
#     return