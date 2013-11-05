# ./plant_extract.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-10-27 21:49:18.637464 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4dd8feca-3f8c-11e3-977f-c82a1455dc46')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: PropertyType
class PropertyType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PropertyType')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 161, 2)
    _Documentation = None
PropertyType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PropertyType, enum_prefix=None)
PropertyType.string = PropertyType._CF_enumeration.addEnumeration(unicode_value=u'string', tag=u'string')
PropertyType.integer = PropertyType._CF_enumeration.addEnumeration(unicode_value=u'integer', tag=u'integer')
PropertyType.float = PropertyType._CF_enumeration.addEnumeration(unicode_value=u'float', tag=u'float')
PropertyType.boolean = PropertyType._CF_enumeration.addEnumeration(unicode_value=u'boolean', tag=u'boolean')
PropertyType.url = PropertyType._CF_enumeration.addEnumeration(unicode_value=u'url', tag=u'url')
PropertyType._InitializeFacetMap(PropertyType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PropertyType', PropertyType)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 5, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element d uses Python identifier d
    __d = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'd'), 'd', '__AbsentNamespace0_CTD_ANON_d', True, pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 7, 8), )

    
    d = property(__d.value, __d.set, None, None)

    
    # Attribute v uses Python identifier v
    __v = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v'), 'v', '__AbsentNamespace0_CTD_ANON_v', pyxb.binding.datatypes.string, unicode_default=u'1')
    __v._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 9, 6)
    __v._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 9, 6)
    
    v = property(__v.value, __v.set, None, None)

    _ElementMap.update({
        __d.name() : __d
    })
    _AttributeMap.update({
        __v.name() : __v
    })



# Complex type DeviceRecord with content type ELEMENT_ONLY
class DeviceRecord (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DeviceRecord with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DeviceRecord')
    _XSDLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 13, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element m uses Python identifier m
    __m = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'm'), 'm', '__AbsentNamespace0_DeviceRecord_m', True, pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 15, 6), )

    
    m = property(__m.value, __m.set, None, None)

    
    # Attribute lid uses Python identifier lid
    __lid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lid'), 'lid', '__AbsentNamespace0_DeviceRecord_lid', pyxb.binding.datatypes.string)
    __lid._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 17, 4)
    __lid._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 17, 4)
    
    lid = property(__lid.value, __lid.set, None, None)

    
    # Attribute ns uses Python identifier ns
    __ns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ns'), 'ns', '__AbsentNamespace0_DeviceRecord_ns', pyxb.binding.datatypes.string, unicode_default=u'mac')
    __ns._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 18, 4)
    __ns._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 18, 4)
    
    ns = property(__ns.value, __ns.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_DeviceRecord_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 19, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 19, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute if uses Python identifier if_
    __if = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'if'), 'if_', '__AbsentNamespace0_DeviceRecord_if', pyxb.binding.datatypes.string, unicode_default=u'0')
    __if._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 20, 4)
    __if._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 20, 4)
    
    if_ = property(__if.value, __if.set, None, None)

    
    # Attribute man uses Python identifier man
    __man = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'man'), 'man', '__AbsentNamespace0_DeviceRecord_man', pyxb.binding.datatypes.string)
    __man._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 21, 4)
    __man._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 21, 4)
    
    man = property(__man.value, __man.set, None, None)

    
    # Attribute mod uses Python identifier mod
    __mod = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mod'), 'mod', '__AbsentNamespace0_DeviceRecord_mod', pyxb.binding.datatypes.string)
    __mod._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 22, 4)
    __mod._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 22, 4)
    
    mod = property(__mod.value, __mod.set, None, None)

    
    # Attribute sn uses Python identifier sn
    __sn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sn'), 'sn', '__AbsentNamespace0_DeviceRecord_sn', pyxb.binding.datatypes.string)
    __sn._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 23, 4)
    __sn._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 23, 4)
    
    sn = property(__sn.value, __sn.set, None, None)

    
    # Attribute t uses Python identifier t
    __t = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u't'), 't', '__AbsentNamespace0_DeviceRecord_t', pyxb.binding.datatypes.string)
    __t._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 24, 4)
    __t._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 24, 4)
    
    t = property(__t.value, __t.set, None, None)

    
    # Attribute cid uses Python identifier cid
    __cid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'cid'), 'cid', '__AbsentNamespace0_DeviceRecord_cid', pyxb.binding.datatypes.string)
    __cid._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 25, 4)
    __cid._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 25, 4)
    
    cid = property(__cid.value, __cid.set, None, None)

    _ElementMap.update({
        __m.name() : __m
    })
    _AttributeMap.update({
        __lid.name() : __lid,
        __ns.name() : __ns,
        __id.name() : __id,
        __if.name() : __if,
        __man.name() : __man,
        __mod.name() : __mod,
        __sn.name() : __sn,
        __t.name() : __t,
        __cid.name() : __cid
    })
Namespace.addCategoryObject('typeBinding', u'DeviceRecord', DeviceRecord)


# Complex type Model with content type ELEMENT_ONLY
class Model (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Model with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Model')
    _XSDLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 28, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'p'), 'p', '__AbsentNamespace0_Model_p', True, pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 30, 6), )

    
    p = property(__p.value, __p.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_Model_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 32, 4)
    __id._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 32, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute ns uses Python identifier ns
    __ns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ns'), 'ns', '__AbsentNamespace0_Model_ns', pyxb.binding.datatypes.string)
    __ns._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 33, 4)
    __ns._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 33, 4)
    
    ns = property(__ns.value, __ns.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__AbsentNamespace0_Model_x', pyxb.binding.datatypes.string)
    __x._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 34, 4)
    __x._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 34, 4)
    
    x = property(__x.value, __x.set, None, None)

    _ElementMap.update({
        __p.name() : __p
    })
    _AttributeMap.update({
        __id.name() : __id,
        __ns.name() : __ns,
        __x.name() : __x
    })
Namespace.addCategoryObject('typeBinding', u'Model', Model)


# Complex type Point with content type SIMPLE
class Point (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Point with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Point')
    _XSDLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 37, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_Point_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 40, 8)
    __id._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 40, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__AbsentNamespace0_Point_x', pyxb.binding.datatypes.string, unicode_default=u'1')
    __x._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 41, 8)
    __x._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 41, 8)
    
    x = property(__x.value, __x.set, None, None)

    
    # Attribute sf uses Python identifier sf
    __sf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sf'), 'sf', '__AbsentNamespace0_Point_sf', pyxb.binding.datatypes.string, unicode_default=u'0')
    __sf._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 42, 8)
    __sf._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 42, 8)
    
    sf = property(__sf.value, __sf.set, None, None)

    
    # Attribute u uses Python identifier u
    __u = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'u'), 'u', '__AbsentNamespace0_Point_u', pyxb.binding.datatypes.string)
    __u._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 43, 8)
    __u._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 43, 8)
    
    u = property(__u.value, __u.set, None, None)

    
    # Attribute d uses Python identifier d
    __d = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'd'), 'd', '__AbsentNamespace0_Point_d', pyxb.binding.datatypes.string)
    __d._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 44, 8)
    __d._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 44, 8)
    
    d = property(__d.value, __d.set, None, None)

    
    # Attribute t uses Python identifier t
    __t = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u't'), 't', '__AbsentNamespace0_Point_t', pyxb.binding.datatypes.string)
    __t._DeclarationLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 45, 8)
    __t._UseLocation = pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 45, 8)
    
    t = property(__t.value, __t.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __x.name() : __x,
        __sf.name() : __sf,
        __u.name() : __u,
        __d.name() : __d,
        __t.name() : __t
    })
Namespace.addCategoryObject('typeBinding', u'Point', Point)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 8, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sunSpecData uses Python identifier sunSpecData
    __sunSpecData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sunSpecData'), 'sunSpecData', '__AbsentNamespace0_CTD_ANON__sunSpecData', False, pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 4, 2), )

    
    sunSpecData = property(__sunSpecData.value, __sunSpecData.set, None, None)

    
    # Element plant uses Python identifier plant
    __plant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'plant'), 'plant', '__AbsentNamespace0_CTD_ANON__plant', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 10, 6), )

    
    plant = property(__plant.value, __plant.set, None, None)

    
    # Element sunSpecMetadata uses Python identifier sunSpecMetadata
    __sunSpecMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sunSpecMetadata'), 'sunSpecMetadata', '__AbsentNamespace0_CTD_ANON__sunSpecMetadata', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 12, 6), )

    
    sunSpecMetadata = property(__sunSpecMetadata.value, __sunSpecMetadata.set, None, None)

    
    # Element strings uses Python identifier strings
    __strings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'strings'), 'strings', '__AbsentNamespace0_CTD_ANON__strings', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 13, 6), )

    
    strings = property(__strings.value, __strings.set, None, None)

    
    # Element extractExtensions uses Python identifier extractExtensions
    __extractExtensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'extractExtensions'), 'extractExtensions', '__AbsentNamespace0_CTD_ANON__extractExtensions', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 14, 6), )

    
    extractExtensions = property(__extractExtensions.value, __extractExtensions.set, None, None)

    
    # Attribute t uses Python identifier t
    __t = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u't'), 't', '__AbsentNamespace0_CTD_ANON__t', pyxb.binding.datatypes.string, required=True)
    __t._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 16, 4)
    __t._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 16, 4)
    
    t = property(__t.value, __t.set, None, None)

    
    # Attribute seqId uses Python identifier seqId
    __seqId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'seqId'), 'seqId', '__AbsentNamespace0_CTD_ANON__seqId', pyxb.binding.datatypes.string)
    __seqId._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 17, 4)
    __seqId._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 17, 4)
    
    seqId = property(__seqId.value, __seqId.set, None, None)

    
    # Attribute lastSeqId uses Python identifier lastSeqId
    __lastSeqId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lastSeqId'), 'lastSeqId', '__AbsentNamespace0_CTD_ANON__lastSeqId', pyxb.binding.datatypes.string)
    __lastSeqId._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 18, 4)
    __lastSeqId._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 18, 4)
    
    lastSeqId = property(__lastSeqId.value, __lastSeqId.set, None, None)

    
    # Attribute v uses Python identifier v
    __v = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v'), 'v', '__AbsentNamespace0_CTD_ANON__v', pyxb.binding.datatypes.string, unicode_default=u'1')
    __v._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 19, 4)
    __v._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 19, 4)
    
    v = property(__v.value, __v.set, None, None)

    _ElementMap.update({
        __sunSpecData.name() : __sunSpecData,
        __plant.name() : __plant,
        __sunSpecMetadata.name() : __sunSpecMetadata,
        __strings.name() : __strings,
        __extractExtensions.name() : __extractExtensions
    })
    _AttributeMap.update({
        __t.name() : __t,
        __seqId.name() : __seqId,
        __lastSeqId.name() : __lastSeqId,
        __v.name() : __v
    })



# Complex type Plant with content type ELEMENT_ONLY
class Plant (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Plant with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Plant')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 25, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element activationDate uses Python identifier activationDate
    __activationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'activationDate'), 'activationDate', '__AbsentNamespace0_Plant_activationDate', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 28, 4), )

    
    activationDate = property(__activationDate.value, __activationDate.set, None, None)

    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'location'), 'location', '__AbsentNamespace0_Plant_location', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 29, 4), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element namePlate uses Python identifier namePlate
    __namePlate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'namePlate'), 'namePlate', '__AbsentNamespace0_Plant_namePlate', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 30, 4), )

    
    namePlate = property(__namePlate.value, __namePlate.set, None, None)

    
    # Element capabilities uses Python identifier capabilities
    __capabilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'capabilities'), 'capabilities', '__AbsentNamespace0_Plant_capabilities', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 31, 4), )

    
    capabilities = property(__capabilities.value, __capabilities.set, None, None)

    
    # Element participant uses Python identifier participant
    __participant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'participant'), 'participant', '__AbsentNamespace0_Plant_participant', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 32, 4), )

    
    participant = property(__participant.value, __participant.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_Plant_name', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_Plant_description', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__AbsentNamespace0_Plant_notes', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__AbsentNamespace0_Plant_label', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_Plant_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 34, 2)
    __id._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 34, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute v uses Python identifier v
    __v = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v'), 'v', '__AbsentNamespace0_Plant_v', pyxb.binding.datatypes.string, unicode_default=u'1')
    __v._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 35, 2)
    __v._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 35, 2)
    
    v = property(__v.value, __v.set, None, None)

    
    # Attribute locale uses Python identifier locale
    __locale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'locale'), 'locale', '__AbsentNamespace0_Plant_locale', pyxb.binding.datatypes.string, unicode_default=u'en')
    __locale._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 36, 2)
    __locale._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 36, 2)
    
    locale = property(__locale.value, __locale.set, None, None)

    _ElementMap.update({
        __activationDate.name() : __activationDate,
        __location.name() : __location,
        __namePlate.name() : __namePlate,
        __capabilities.name() : __capabilities,
        __participant.name() : __participant,
        __name.name() : __name,
        __description.name() : __description,
        __notes.name() : __notes,
        __label.name() : __label
    })
    _AttributeMap.update({
        __id.name() : __id,
        __v.name() : __v,
        __locale.name() : __locale
    })
Namespace.addCategoryObject('typeBinding', u'Plant', Plant)


# Complex type Location with content type ELEMENT_ONLY
class Location (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Location with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Location')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 39, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element latitude uses Python identifier latitude
    __latitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'latitude'), 'latitude', '__AbsentNamespace0_Location_latitude', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 41, 4), )

    
    latitude = property(__latitude.value, __latitude.set, None, None)

    
    # Element longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'longitude'), 'longitude', '__AbsentNamespace0_Location_longitude', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 42, 4), )

    
    longitude = property(__longitude.value, __longitude.set, None, None)

    
    # Element line1 uses Python identifier line1
    __line1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'line1'), 'line1', '__AbsentNamespace0_Location_line1', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 43, 4), )

    
    line1 = property(__line1.value, __line1.set, None, None)

    
    # Element line2 uses Python identifier line2
    __line2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'line2'), 'line2', '__AbsentNamespace0_Location_line2', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 44, 4), )

    
    line2 = property(__line2.value, __line2.set, None, None)

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'city'), 'city', '__AbsentNamespace0_Location_city', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 45, 4), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element stateProvince uses Python identifier stateProvince
    __stateProvince = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'stateProvince'), 'stateProvince', '__AbsentNamespace0_Location_stateProvince', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 46, 4), )

    
    stateProvince = property(__stateProvince.value, __stateProvince.set, None, None)

    
    # Element country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'country'), 'country', '__AbsentNamespace0_Location_country', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 47, 4), )

    
    country = property(__country.value, __country.set, None, None)

    
    # Element postal uses Python identifier postal
    __postal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'postal'), 'postal', '__AbsentNamespace0_Location_postal', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 48, 4), )

    
    postal = property(__postal.value, __postal.set, None, None)

    
    # Element elevation uses Python identifier elevation
    __elevation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'elevation'), 'elevation', '__AbsentNamespace0_Location_elevation', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 49, 4), )

    
    elevation = property(__elevation.value, __elevation.set, None, None)

    
    # Element timezone uses Python identifier timezone
    __timezone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'timezone'), 'timezone', '__AbsentNamespace0_Location_timezone', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 50, 4), )

    
    timezone = property(__timezone.value, __timezone.set, None, None)

    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property'), 'property_', '__AbsentNamespace0_Location_property', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 51, 4), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __latitude.name() : __latitude,
        __longitude.name() : __longitude,
        __line1.name() : __line1,
        __line2.name() : __line2,
        __city.name() : __city,
        __stateProvince.name() : __stateProvince,
        __country.name() : __country,
        __postal.name() : __postal,
        __elevation.name() : __elevation,
        __timezone.name() : __timezone,
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Location', Location)


# Complex type NamePlate with content type ELEMENT_ONLY
class NamePlate (pyxb.binding.basis.complexTypeDefinition):
    """Complex type NamePlate with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NamePlate')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 55, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property'), 'property_', '__AbsentNamespace0_NamePlate_property', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 57, 4), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'NamePlate', NamePlate)


# Complex type Capabilities with content type ELEMENT_ONLY
class Capabilities (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Capabilities with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Capabilities')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 61, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property'), 'property_', '__AbsentNamespace0_Capabilities_property', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 63, 4), )

    
    property_ = property(__property.value, __property.set, None, None)

    _ElementMap.update({
        __property.name() : __property
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Capabilities', Capabilities)


# Complex type Participant with content type ELEMENT_ONLY
class Participant (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Participant with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Participant')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 67, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property'), 'property_', '__AbsentNamespace0_Participant_property', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 69, 4), )

    
    property_ = property(__property.value, __property.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_Participant_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 71, 2)
    __type._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 71, 2)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __property.name() : __property
    })
    _AttributeMap.update({
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'Participant', Participant)


# Complex type SunSpecMetadata with content type ELEMENT_ONLY
class SunSpecMetadata (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SunSpecMetadata with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SunSpecMetadata')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 76, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element d uses Python identifier d
    __d = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'd'), 'd', '__AbsentNamespace0_SunSpecMetadata_d', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 78, 4), )

    
    d = property(__d.value, __d.set, None, None)

    _ElementMap.update({
        __d.name() : __d
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SunSpecMetadata', SunSpecMetadata)


# Complex type DeviceRecordMetadata with content type ELEMENT_ONLY
class DeviceRecordMetadata (pyxb.binding.basis.complexTypeDefinition):
    """Complex type DeviceRecordMetadata with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DeviceRecordMetadata')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 83, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property'), 'property_', '__AbsentNamespace0_DeviceRecordMetadata_property', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 86, 6), )

    
    property_ = property(__property.value, __property.set, None, None)

    
    # Element m uses Python identifier m
    __m = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'm'), 'm', '__AbsentNamespace0_DeviceRecordMetadata_m', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 87, 6), )

    
    m = property(__m.value, __m.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_DeviceRecordMetadata_name', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_DeviceRecordMetadata_description', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__AbsentNamespace0_DeviceRecordMetadata_notes', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__AbsentNamespace0_DeviceRecordMetadata_label', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute lid uses Python identifier lid
    __lid = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'lid'), 'lid', '__AbsentNamespace0_DeviceRecordMetadata_lid', pyxb.binding.datatypes.string)
    __lid._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 89, 4)
    __lid._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 89, 4)
    
    lid = property(__lid.value, __lid.set, None, None)

    
    # Attribute ns uses Python identifier ns
    __ns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ns'), 'ns', '__AbsentNamespace0_DeviceRecordMetadata_ns', pyxb.binding.datatypes.string, unicode_default=u'mac')
    __ns._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 90, 4)
    __ns._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 90, 4)
    
    ns = property(__ns.value, __ns.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_DeviceRecordMetadata_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 91, 4)
    __id._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 91, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute if uses Python identifier if_
    __if = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'if'), 'if_', '__AbsentNamespace0_DeviceRecordMetadata_if', pyxb.binding.datatypes.string, unicode_default=u'0')
    __if._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 92, 4)
    __if._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 92, 4)
    
    if_ = property(__if.value, __if.set, None, None)

    
    # Attribute man uses Python identifier man
    __man = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'man'), 'man', '__AbsentNamespace0_DeviceRecordMetadata_man', pyxb.binding.datatypes.string)
    __man._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 93, 4)
    __man._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 93, 4)
    
    man = property(__man.value, __man.set, None, None)

    
    # Attribute mod uses Python identifier mod
    __mod = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mod'), 'mod', '__AbsentNamespace0_DeviceRecordMetadata_mod', pyxb.binding.datatypes.string)
    __mod._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 94, 4)
    __mod._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 94, 4)
    
    mod = property(__mod.value, __mod.set, None, None)

    
    # Attribute sn uses Python identifier sn
    __sn = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sn'), 'sn', '__AbsentNamespace0_DeviceRecordMetadata_sn', pyxb.binding.datatypes.string)
    __sn._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 95, 4)
    __sn._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 95, 4)
    
    sn = property(__sn.value, __sn.set, None, None)

    _ElementMap.update({
        __property.name() : __property,
        __m.name() : __m,
        __name.name() : __name,
        __description.name() : __description,
        __notes.name() : __notes,
        __label.name() : __label
    })
    _AttributeMap.update({
        __lid.name() : __lid,
        __ns.name() : __ns,
        __id.name() : __id,
        __if.name() : __if,
        __man.name() : __man,
        __mod.name() : __mod,
        __sn.name() : __sn
    })
Namespace.addCategoryObject('typeBinding', u'DeviceRecordMetadata', DeviceRecordMetadata)


# Complex type ModelMetadata with content type ELEMENT_ONLY
class ModelMetadata (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ModelMetadata with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModelMetadata')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 98, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property'), 'property_', '__AbsentNamespace0_ModelMetadata_property', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 101, 6), )

    
    property_ = property(__property.value, __property.set, None, None)

    
    # Element p uses Python identifier p
    __p = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'p'), 'p', '__AbsentNamespace0_ModelMetadata_p', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 102, 6), )

    
    p = property(__p.value, __p.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_ModelMetadata_name', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_ModelMetadata_description', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__AbsentNamespace0_ModelMetadata_notes', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__AbsentNamespace0_ModelMetadata_label', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_ModelMetadata_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 104, 4)
    __id._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 104, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute ns uses Python identifier ns
    __ns = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ns'), 'ns', '__AbsentNamespace0_ModelMetadata_ns', pyxb.binding.datatypes.string)
    __ns._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 105, 4)
    __ns._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 105, 4)
    
    ns = property(__ns.value, __ns.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__AbsentNamespace0_ModelMetadata_x', pyxb.binding.datatypes.string)
    __x._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 106, 4)
    __x._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 106, 4)
    
    x = property(__x.value, __x.set, None, None)

    _ElementMap.update({
        __property.name() : __property,
        __p.name() : __p,
        __name.name() : __name,
        __description.name() : __description,
        __notes.name() : __notes,
        __label.name() : __label
    })
    _AttributeMap.update({
        __id.name() : __id,
        __ns.name() : __ns,
        __x.name() : __x
    })
Namespace.addCategoryObject('typeBinding', u'ModelMetadata', ModelMetadata)


# Complex type PointMetadata with content type ELEMENT_ONLY
class PointMetadata (pyxb.binding.basis.complexTypeDefinition):
    """Complex type PointMetadata with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PointMetadata')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 109, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element property uses Python identifier property_
    __property = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'property'), 'property_', '__AbsentNamespace0_PointMetadata_property', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 112, 6), )

    
    property_ = property(__property.value, __property.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_PointMetadata_name', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_PointMetadata_description', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__AbsentNamespace0_PointMetadata_notes', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__AbsentNamespace0_PointMetadata_label', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_PointMetadata_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 114, 4)
    __id._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 114, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'x'), 'x', '__AbsentNamespace0_PointMetadata_x', pyxb.binding.datatypes.string, unicode_default=u'1')
    __x._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 115, 4)
    __x._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 115, 4)
    
    x = property(__x.value, __x.set, None, None)

    _ElementMap.update({
        __property.name() : __property,
        __name.name() : __name,
        __description.name() : __description,
        __notes.name() : __notes,
        __label.name() : __label
    })
    _AttributeMap.update({
        __id.name() : __id,
        __x.name() : __x
    })
Namespace.addCategoryObject('typeBinding', u'PointMetadata', PointMetadata)


# Complex type Strings with content type ELEMENT_ONLY
class Strings (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Strings with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Strings')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 120, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element plant uses Python identifier plant
    __plant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'plant'), 'plant', '__AbsentNamespace0_Strings_plant', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 122, 4), )

    
    plant = property(__plant.value, __plant.set, None, None)

    
    # Element sunSpecMetadata uses Python identifier sunSpecMetadata
    __sunSpecMetadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'sunSpecMetadata'), 'sunSpecMetadata', '__AbsentNamespace0_Strings_sunSpecMetadata', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 123, 4), )

    
    sunSpecMetadata = property(__sunSpecMetadata.value, __sunSpecMetadata.set, None, None)

    
    # Attribute locale uses Python identifier locale
    __locale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'locale'), 'locale', '__AbsentNamespace0_Strings_locale', pyxb.binding.datatypes.string, required=True)
    __locale._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 125, 2)
    __locale._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 125, 2)
    
    locale = property(__locale.value, __locale.set, None, None)

    _ElementMap.update({
        __plant.name() : __plant,
        __sunSpecMetadata.name() : __sunSpecMetadata
    })
    _AttributeMap.update({
        __locale.name() : __locale
    })
Namespace.addCategoryObject('typeBinding', u'Strings', Strings)


# Complex type StringsPlant with content type ELEMENT_ONLY
class StringsPlant (pyxb.binding.basis.complexTypeDefinition):
    """Complex type StringsPlant with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StringsPlant')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 128, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element participant uses Python identifier participant
    __participant = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'participant'), 'participant', '__AbsentNamespace0_StringsPlant_participant', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 131, 4), )

    
    participant = property(__participant.value, __participant.set, None, None)

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_StringsPlant_name', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_StringsPlant_description', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__AbsentNamespace0_StringsPlant_notes', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__AbsentNamespace0_StringsPlant_label', False, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4), )

    
    label = property(__label.value, __label.set, None, None)

    _ElementMap.update({
        __participant.name() : __participant,
        __name.name() : __name,
        __description.name() : __description,
        __notes.name() : __notes,
        __label.name() : __label
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'StringsPlant', StringsPlant)


# Complex type Extensions with content type ELEMENT_ONLY
class Extensions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Extensions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Extensions')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 137, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element extension uses Python identifier extension
    __extension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'extension'), 'extension', '__AbsentNamespace0_Extensions_extension', True, pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 139, 4), )

    
    extension = property(__extension.value, __extension.set, None, None)

    _ElementMap.update({
        __extension.name() : __extension
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'Extensions', Extensions)


# Complex type Extension with content type ELEMENT_ONLY
class Extension (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Extension with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Extension')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 143, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'name'), 'name', '__AbsentNamespace0_Extension_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 147, 2)
    __name._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 147, 2)
    
    name = property(__name.value, __name.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', u'Extension', Extension)


# Complex type Property with content type SIMPLE
class Property (pyxb.binding.basis.complexTypeDefinition):
    """Complex type Property with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Property')
    _XSDLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 152, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_Property_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 155, 8)
    __id._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 155, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_Property_type', PropertyType, unicode_default=u'string')
    __type._DeclarationLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 156, 8)
    __type._UseLocation = pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 156, 8)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'Property', Property)


sunSpecData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sunSpecData'), CTD_ANON, location=pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', sunSpecData.name().localName(), sunSpecData)

sunSpecPlantExtract = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sunSpecPlantExtract'), CTD_ANON_, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 7, 1))
Namespace.addCategoryObject('elementBinding', sunSpecPlantExtract.name().localName(), sunSpecPlantExtract)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'd'), DeviceRecord, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 7, 8)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 7, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'd')), pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 7, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




DeviceRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'm'), Model, scope=DeviceRecord, location=pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 15, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 15, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DeviceRecord._UseForTag(pyxb.namespace.ExpandedName(None, u'm')), pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 15, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DeviceRecord._Automaton = _BuildAutomaton_()




Model._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'p'), Point, scope=Model, location=pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 30, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 30, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Model._UseForTag(pyxb.namespace.ExpandedName(None, u'p')), pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 30, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Model._Automaton = _BuildAutomaton_2()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sunSpecData'), CTD_ANON, scope=CTD_ANON_, location=pyxb.utils.utility.Location(u'xsd/sunspec_data.xsd', 4, 2)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'plant'), Plant, scope=CTD_ANON_, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 10, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sunSpecMetadata'), SunSpecMetadata, scope=CTD_ANON_, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 12, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'strings'), Strings, scope=CTD_ANON_, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 13, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'extractExtensions'), Extensions, scope=CTD_ANON_, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 14, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 11, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 12, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 13, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 14, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'plant')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 10, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sunSpecData')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 11, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'sunSpecMetadata')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 12, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'strings')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 13, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(None, u'extractExtensions')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 14, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_._Automaton = _BuildAutomaton_3()




Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'activationDate'), pyxb.binding.datatypes.string, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 28, 4)))

Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'location'), Location, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 29, 4)))

Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'namePlate'), NamePlate, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 30, 4)))

Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'capabilities'), Capabilities, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 31, 4)))

Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'participant'), Participant, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 32, 4)))

Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4)))

Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4)))

Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4)))

Plant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'label'), pyxb.binding.datatypes.string, scope=Plant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 28, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 29, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 30, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 31, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 32, 4))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'label')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'activationDate')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 28, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'location')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 29, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'namePlate')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 30, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'capabilities')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 31, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Plant._UseForTag(pyxb.namespace.ExpandedName(None, u'participant')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 32, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Plant._Automaton = _BuildAutomaton_4()




Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'latitude'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 41, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'longitude'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 42, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'line1'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 43, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'line2'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 44, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'city'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 45, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'stateProvince'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 46, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'country'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 47, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'postal'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 48, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'elevation'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 49, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'timezone'), pyxb.binding.datatypes.string, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 50, 4)))

Location._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property'), Property, scope=Location, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 51, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 41, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 42, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 43, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 44, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 45, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 46, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 47, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 48, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 49, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 50, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 51, 4))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'latitude')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 41, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'longitude')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 42, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'line1')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 43, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'line2')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 44, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'city')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 45, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'stateProvince')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 46, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'country')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 47, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'postal')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 48, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'elevation')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 49, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'timezone')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 50, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Location._UseForTag(pyxb.namespace.ExpandedName(None, u'property')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 51, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Location._Automaton = _BuildAutomaton_5()




NamePlate._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property'), Property, scope=NamePlate, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 57, 4)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 57, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(NamePlate._UseForTag(pyxb.namespace.ExpandedName(None, u'property')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 57, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NamePlate._Automaton = _BuildAutomaton_6()




Capabilities._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property'), Property, scope=Capabilities, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 63, 4)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 63, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Capabilities._UseForTag(pyxb.namespace.ExpandedName(None, u'property')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 63, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Capabilities._Automaton = _BuildAutomaton_7()




Participant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property'), Property, scope=Participant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 69, 4)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 69, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Participant._UseForTag(pyxb.namespace.ExpandedName(None, u'property')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 69, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Participant._Automaton = _BuildAutomaton_8()




SunSpecMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'd'), DeviceRecordMetadata, scope=SunSpecMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 78, 4)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 78, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SunSpecMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'd')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 78, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SunSpecMetadata._Automaton = _BuildAutomaton_9()




DeviceRecordMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property'), Property, scope=DeviceRecordMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 86, 6)))

DeviceRecordMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'm'), ModelMetadata, scope=DeviceRecordMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 87, 6)))

DeviceRecordMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=DeviceRecordMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4)))

DeviceRecordMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=DeviceRecordMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4)))

DeviceRecordMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=DeviceRecordMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4)))

DeviceRecordMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'label'), pyxb.binding.datatypes.string, scope=DeviceRecordMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 86, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 87, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DeviceRecordMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DeviceRecordMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DeviceRecordMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DeviceRecordMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'label')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DeviceRecordMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'property')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 86, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DeviceRecordMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'm')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 87, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DeviceRecordMetadata._Automaton = _BuildAutomaton_10()




ModelMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property'), Property, scope=ModelMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 101, 6)))

ModelMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'p'), PointMetadata, scope=ModelMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 102, 6)))

ModelMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=ModelMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4)))

ModelMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=ModelMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4)))

ModelMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=ModelMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4)))

ModelMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'label'), pyxb.binding.datatypes.string, scope=ModelMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 101, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 102, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ModelMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ModelMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ModelMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'label')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ModelMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'property')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 101, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ModelMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'p')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 102, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ModelMetadata._Automaton = _BuildAutomaton_11()




PointMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'property'), Property, scope=PointMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 112, 6)))

PointMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=PointMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4)))

PointMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=PointMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4)))

PointMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=PointMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4)))

PointMetadata._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'label'), pyxb.binding.datatypes.string, scope=PointMetadata, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 112, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PointMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PointMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(PointMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(PointMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'label')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(PointMetadata._UseForTag(pyxb.namespace.ExpandedName(None, u'property')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 112, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PointMetadata._Automaton = _BuildAutomaton_12()




Strings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'plant'), StringsPlant, scope=Strings, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 122, 4)))

Strings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'sunSpecMetadata'), SunSpecMetadata, scope=Strings, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 123, 4)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 122, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 123, 4))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Strings._UseForTag(pyxb.namespace.ExpandedName(None, u'plant')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 122, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Strings._UseForTag(pyxb.namespace.ExpandedName(None, u'sunSpecMetadata')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 123, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
Strings._Automaton = _BuildAutomaton_13()




StringsPlant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'participant'), Participant, scope=StringsPlant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 131, 4)))

StringsPlant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'name'), pyxb.binding.datatypes.string, scope=StringsPlant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4)))

StringsPlant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=StringsPlant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4)))

StringsPlant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=StringsPlant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4)))

StringsPlant._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'label'), pyxb.binding.datatypes.string, scope=StringsPlant, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 131, 4))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StringsPlant._UseForTag(pyxb.namespace.ExpandedName(None, u'name')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 173, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StringsPlant._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 174, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StringsPlant._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 175, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(StringsPlant._UseForTag(pyxb.namespace.ExpandedName(None, u'label')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 176, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(StringsPlant._UseForTag(pyxb.namespace.ExpandedName(None, u'participant')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 131, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StringsPlant._Automaton = _BuildAutomaton_14()




Extensions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'extension'), Extension, scope=Extensions, location=pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 139, 4)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Extensions._UseForTag(pyxb.namespace.ExpandedName(None, u'extension')), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 139, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Extensions._Automaton = _BuildAutomaton_15()




def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, None)), pyxb.utils.utility.Location('xsd/sunspec_plant_extract.xsd', 145, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Extension._Automaton = _BuildAutomaton_16()

