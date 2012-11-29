from collections import defaultdict
import hashlib
import os
import logging

from lxml import etree
from lxml import objectify


smdx_dir    = "smdx/files"
smdx_prefix = "smdx"
smdx_ext    = ".xml"
smdx_xsd    = "smdx.xsd"
smdx_schema_parser = None

# SMDX descriptive model id constants
INVERTER_SINGLE_PHASE = '101'
INVERTER_SPLIT_PHASE  = '102'
INVERTER_THREE_PHASE  = '103'
METER_SINGLE_PHASE    = '201'



class SMDX(object):
    _cache={}

    # TODO: Turn this into a factory returning the same SMDX if requested multiple times

    def __init__(self, element, model_id):
        logging.debug("SMDX.__init__()")
        return
        
    def __new__(cls, element, model_id):
        try:
            return SMDX._cache[model_id]
        except KeyError:
            logging.info("New SMDX object being instantiated for: " + model_id)
            # you must call __new__ on the base class
            x = super(SMDX, cls).__new__(cls)

            x.points = {}
            x.smdx_tree = None
            x.model_id = model_id
            smdx_filename = smdx_prefix + "_" + str.rjust(str(x.model_id), 5, "0") + smdx_ext
            print element, model_id, smdx_filename
            parser = get_smdx_parser()
            
            try:
              x.smdx_tree = objectify.parse(os.path.join(os.getcwd(), smdx_dir, smdx_filename), 
                                            parser)
            except IOError:
              logging.error("IOError caught while opening " + smdx_filename)
              
            if (x.smdx_tree is None):
              raise SunSpecSMDXException("SMDX object requires valid SMDX file: " + smdx_filename)
    
            x.__init__(element, model_id)
            SMDX._cache[model_id] = x
            logging.info("SMDX Cache: " + str(SMDX._cache))
            
            return x

    def get_points(self):
        root = self.smdx_tree.getroot()
        for b in root.model.block:
            for p in b.point:
                p_id = p.get('id')
                self.points[p_id] = SMDXPoint(p)
    
        return self.points

    def get_mandatory_points(self):
        man_points = {}
        points = self.get_points()
        for p in points.itervalues():
            if p.mandatory:
                man_points[p.id] = p
   
        return man_points


class SMDXPoint(object):
  '''SMDX Point class that understands points like:
    <point id="PhVphA" offset="8" type="uint16" sf="V_SF" units="V" mandatory="true" />
  '''
  def __init__(self, element):
    element = element
    if (element is None) or (element.tag != 'point'):
      logging.warning("SMDXPoint objects must have a 'point' element")
      return
    
    self.id     = element.get('id')
    logging.debug("SMDXPoint.__init__() self.id: " + self.id)
    self.len    = element.get('len')
    self.offset = element.get('offset')
    self.type   = element.get('type')
    self.sf     = element.get('sf')
    self.units  = element.get('units')
    self.access = element.get('access')
    self.mandatory = False
    mand = element.get('mandatory')
    if mand is not None:
      self.mandatory = True if (mand.lower() == "true") else False
    
    logging.debug("SMDXPoint.__init__() self.mandatory: " + str(self.mandatory))


class SunSpecSMDXException(Exception):
  
  def __init__(self, argument):
    super(SunSpecSMDXException, self).__init__(argument)
    self.argument = argument


def get_smdx_parser():
  global smdx_schema_parser
  if (smdx_schema_parser is None):
    try:
      schema_filename = os.path.join(os.getcwd(), smdx_dir, smdx_xsd)
      schema_etree = etree.parse(schema_filename)
      schema = etree.XMLSchema(schema_etree)
      logging.info("get_smdx_parser() getting a global lxml.objectify SMDX parser")
      smdx_schema_parser = objectify.makeparser(schema = schema)
    except IOError:
      logging.error("IOError caught while opening " + schema_filename)

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