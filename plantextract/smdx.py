# ./smdx_gen.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2013-10-27 00:48:37.033045 by PyXB version 1.2.3
# Namespace AbsentNamespace0

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:2ff6e4c2-3edc-11e3-b9a4-c82a1455dc46')

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


# Atomic simple type: PointTypeDefinition
class PointTypeDefinition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PointTypeDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 106, 2)
    _Documentation = None
PointTypeDefinition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PointTypeDefinition, enum_prefix=None)
PointTypeDefinition.int16 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'int16', tag=u'int16')
PointTypeDefinition.uint16 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'uint16', tag=u'uint16')
PointTypeDefinition.acc16 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'acc16', tag=u'acc16')
PointTypeDefinition.int32 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'int32', tag=u'int32')
PointTypeDefinition.uint32 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'uint32', tag=u'uint32')
PointTypeDefinition.float32 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'float32', tag=u'float32')
PointTypeDefinition.acc32 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'acc32', tag=u'acc32')
PointTypeDefinition.int64 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'int64', tag=u'int64')
PointTypeDefinition.uint64 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'uint64', tag=u'uint64')
PointTypeDefinition.float64 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'float64', tag=u'float64')
PointTypeDefinition.acc64 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'acc64', tag=u'acc64')
PointTypeDefinition.enum16 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'enum16', tag=u'enum16')
PointTypeDefinition.enum32 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'enum32', tag=u'enum32')
PointTypeDefinition.bitfield16 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'bitfield16', tag=u'bitfield16')
PointTypeDefinition.bitfield32 = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'bitfield32', tag=u'bitfield32')
PointTypeDefinition.sunssf = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'sunssf', tag=u'sunssf')
PointTypeDefinition.string = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'string', tag=u'string')
PointTypeDefinition.pad = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'pad', tag=u'pad')
PointTypeDefinition.ipaddr = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'ipaddr', tag=u'ipaddr')
PointTypeDefinition.ipv6addr = PointTypeDefinition._CF_enumeration.addEnumeration(unicode_value=u'ipv6addr', tag=u'ipv6addr')
PointTypeDefinition._InitializeFacetMap(PointTypeDefinition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PointTypeDefinition', PointTypeDefinition)

# Atomic simple type: PointAccessDefinition
class PointAccessDefinition (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PointAccessDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 131, 2)
    _Documentation = None
PointAccessDefinition._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=PointAccessDefinition, enum_prefix=None)
PointAccessDefinition.r = PointAccessDefinition._CF_enumeration.addEnumeration(unicode_value=u'r', tag=u'r')
PointAccessDefinition.rw = PointAccessDefinition._CF_enumeration.addEnumeration(unicode_value=u'rw', tag=u'rw')
PointAccessDefinition.w = PointAccessDefinition._CF_enumeration.addEnumeration(unicode_value=u'w', tag=u'w')
PointAccessDefinition._InitializeFacetMap(PointAccessDefinition._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'PointAccessDefinition', PointAccessDefinition)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 17, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element model uses Python identifier model
    __model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'model'), 'model', '__AbsentNamespace0_CTD_ANON_model', True, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 27, 6), )

    
    model = property(__model.value, __model.set, None, None)

    
    # Element strings uses Python identifier strings
    __strings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'strings'), 'strings', '__AbsentNamespace0_CTD_ANON_strings', True, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 28, 6), )

    
    strings = property(__strings.value, __strings.set, None, None)

    
    # Attribute v uses Python identifier v
    __v = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'v'), 'v', '__AbsentNamespace0_CTD_ANON_v', pyxb.binding.datatypes.string, unicode_default=u'1')
    __v._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 21, 6)
    __v._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 21, 6)
    
    v = property(__v.value, __v.set, None, None)

    _ElementMap.update({
        __model.name() : __model,
        __strings.name() : __strings
    })
    _AttributeMap.update({
        __v.name() : __v
    })



# Complex type ModelDefinition with content type ELEMENT_ONLY
class ModelDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ModelDefinition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ModelDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 32, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element block uses Python identifier block
    __block = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'block'), 'block', '__AbsentNamespace0_ModelDefinition_block', True, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 34, 6), )

    
    block = property(__block.value, __block.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_ModelDefinition_id', pyxb.binding.datatypes.integer)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 36, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 36, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute len uses Python identifier len
    __len = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'len'), 'len', '__AbsentNamespace0_ModelDefinition_len', pyxb.binding.datatypes.integer)
    __len._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 37, 4)
    __len._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 37, 4)
    
    len = property(__len.value, __len.set, None, None)

    _ElementMap.update({
        __block.name() : __block
    })
    _AttributeMap.update({
        __id.name() : __id,
        __len.name() : __len
    })
Namespace.addCategoryObject('typeBinding', u'ModelDefinition', ModelDefinition)


# Complex type BlockDefinition with content type ELEMENT_ONLY
class BlockDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BlockDefinition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'BlockDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 40, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'point'), 'point', '__AbsentNamespace0_BlockDefinition_point', True, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 42, 6), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Attribute len uses Python identifier len
    __len = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'len'), 'len', '__AbsentNamespace0_BlockDefinition_len', pyxb.binding.datatypes.integer)
    __len._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 44, 4)
    __len._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 44, 4)
    
    len = property(__len.value, __len.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_BlockDefinition_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 45, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 45, 4)
    
    type = property(__type.value, __type.set, None, None)

    _ElementMap.update({
        __point.name() : __point
    })
    _AttributeMap.update({
        __len.name() : __len,
        __type.name() : __type
    })
Namespace.addCategoryObject('typeBinding', u'BlockDefinition', BlockDefinition)


# Complex type SymbolDefinition with content type SIMPLE
class SymbolDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type SymbolDefinition with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SymbolDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 62, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_SymbolDefinition_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 65, 8)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 65, 8)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', u'SymbolDefinition', SymbolDefinition)


# Complex type StringsDefinition with content type ELEMENT_ONLY
class StringsDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type StringsDefinition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StringsDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element model uses Python identifier model
    __model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'model'), 'model', '__AbsentNamespace0_StringsDefinition_model', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 72, 6), )

    
    model = property(__model.value, __model.set, None, None)

    
    # Element point uses Python identifier point
    __point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'point'), 'point', '__AbsentNamespace0_StringsDefinition_point', True, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 73, 6), )

    
    point = property(__point.value, __point.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_StringsDefinition_id', pyxb.binding.datatypes.integer, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 75, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 75, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute locale uses Python identifier locale
    __locale = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'locale'), 'locale', '__AbsentNamespace0_StringsDefinition_locale', pyxb.binding.datatypes.string)
    __locale._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 76, 4)
    __locale._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 76, 4)
    
    locale = property(__locale.value, __locale.set, None, None)

    _ElementMap.update({
        __model.name() : __model,
        __point.name() : __point
    })
    _AttributeMap.update({
        __id.name() : __id,
        __locale.name() : __locale
    })
Namespace.addCategoryObject('typeBinding', u'StringsDefinition', StringsDefinition)


# Complex type StringsModelDefinition with content type ELEMENT_ONLY
class StringsModelDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type StringsModelDefinition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StringsModelDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 79, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__AbsentNamespace0_StringsModelDefinition_label', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 81, 6), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_StringsModelDefinition_description', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 82, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__AbsentNamespace0_StringsModelDefinition_notes', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 83, 6), )

    
    notes = property(__notes.value, __notes.set, None, None)

    _ElementMap.update({
        __label.name() : __label,
        __description.name() : __description,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'StringsModelDefinition', StringsModelDefinition)


# Complex type StringsPointDefinition with content type ELEMENT_ONLY
class StringsPointDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type StringsPointDefinition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StringsPointDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 87, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__AbsentNamespace0_StringsPointDefinition_label', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 89, 6), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_StringsPointDefinition_description', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 90, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__AbsentNamespace0_StringsPointDefinition_notes', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 91, 6), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Element symbol uses Python identifier symbol
    __symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'symbol'), 'symbol', '__AbsentNamespace0_StringsPointDefinition_symbol', True, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 92, 6), )

    
    symbol = property(__symbol.value, __symbol.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_StringsPointDefinition_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 94, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 94, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __label.name() : __label,
        __description.name() : __description,
        __notes.name() : __notes,
        __symbol.name() : __symbol
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', u'StringsPointDefinition', StringsPointDefinition)


# Complex type StringsSymbolDefinition with content type ELEMENT_ONLY
class StringsSymbolDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type StringsSymbolDefinition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StringsSymbolDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 97, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element label uses Python identifier label
    __label = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'label'), 'label', '__AbsentNamespace0_StringsSymbolDefinition_label', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 99, 6), )

    
    label = property(__label.value, __label.set, None, None)

    
    # Element description uses Python identifier description
    __description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'description'), 'description', '__AbsentNamespace0_StringsSymbolDefinition_description', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 100, 6), )

    
    description = property(__description.value, __description.set, None, None)

    
    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'notes'), 'notes', '__AbsentNamespace0_StringsSymbolDefinition_notes', False, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 101, 6), )

    
    notes = property(__notes.value, __notes.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_StringsSymbolDefinition_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 103, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 103, 4)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        __label.name() : __label,
        __description.name() : __description,
        __notes.name() : __notes
    })
    _AttributeMap.update({
        __id.name() : __id
    })
Namespace.addCategoryObject('typeBinding', u'StringsSymbolDefinition', StringsSymbolDefinition)


# Complex type PointDefinition with content type ELEMENT_ONLY
class PointDefinition (pyxb.binding.basis.complexTypeDefinition):
    """Complex type PointDefinition with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PointDefinition')
    _XSDLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 48, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element symbol uses Python identifier symbol
    __symbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'symbol'), 'symbol', '__AbsentNamespace0_PointDefinition_symbol', True, pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 50, 6), )

    
    symbol = property(__symbol.value, __symbol.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'id'), 'id', '__AbsentNamespace0_PointDefinition_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 52, 4)
    __id._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 52, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute len uses Python identifier len
    __len = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'len'), 'len', '__AbsentNamespace0_PointDefinition_len', pyxb.binding.datatypes.integer)
    __len._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 53, 4)
    __len._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 53, 4)
    
    len = property(__len.value, __len.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'offset'), 'offset', '__AbsentNamespace0_PointDefinition_offset', pyxb.binding.datatypes.integer)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 54, 4)
    __offset._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 54, 4)
    
    offset = property(__offset.value, __offset.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'type'), 'type', '__AbsentNamespace0_PointDefinition_type', PointTypeDefinition)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 55, 4)
    __type._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 55, 4)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute sf uses Python identifier sf
    __sf = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'sf'), 'sf', '__AbsentNamespace0_PointDefinition_sf', pyxb.binding.datatypes.string)
    __sf._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 56, 4)
    __sf._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 56, 4)
    
    sf = property(__sf.value, __sf.set, None, None)

    
    # Attribute units uses Python identifier units
    __units = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'units'), 'units', '__AbsentNamespace0_PointDefinition_units', pyxb.binding.datatypes.string)
    __units._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 57, 4)
    __units._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 57, 4)
    
    units = property(__units.value, __units.set, None, None)

    
    # Attribute access uses Python identifier access
    __access = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'access'), 'access', '__AbsentNamespace0_PointDefinition_access', PointAccessDefinition)
    __access._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 58, 4)
    __access._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 58, 4)
    
    access = property(__access.value, __access.set, None, None)

    
    # Attribute mandatory uses Python identifier mandatory
    __mandatory = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'mandatory'), 'mandatory', '__AbsentNamespace0_PointDefinition_mandatory', pyxb.binding.datatypes.boolean)
    __mandatory._DeclarationLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 59, 4)
    __mandatory._UseLocation = pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 59, 4)
    
    mandatory = property(__mandatory.value, __mandatory.set, None, None)

    _ElementMap.update({
        __symbol.name() : __symbol
    })
    _AttributeMap.update({
        __id.name() : __id,
        __len.name() : __len,
        __offset.name() : __offset,
        __type.name() : __type,
        __sf.name() : __sf,
        __units.name() : __units,
        __access.name() : __access,
        __mandatory.name() : __mandatory
    })
Namespace.addCategoryObject('typeBinding', u'PointDefinition', PointDefinition)


sunSpecModels = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sunSpecModels'), CTD_ANON, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 16, 2))
Namespace.addCategoryObject('elementBinding', sunSpecModels.name().localName(), sunSpecModels)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'model'), ModelDefinition, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 27, 6)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'strings'), StringsDefinition, scope=CTD_ANON, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 28, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 19, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 27, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 28, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'model')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 27, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(None, u'strings')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 28, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




ModelDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'block'), BlockDefinition, scope=ModelDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 34, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=2L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 34, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ModelDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'block')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 34, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ModelDefinition._Automaton = _BuildAutomaton_()




BlockDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'point'), PointDefinition, scope=BlockDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 42, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 42, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BlockDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'point')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 42, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BlockDefinition._Automaton = _BuildAutomaton_2()




StringsDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'model'), StringsModelDefinition, scope=StringsDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 72, 6)))

StringsDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'point'), StringsPointDefinition, scope=StringsDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 73, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 72, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 73, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StringsDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'model')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 72, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StringsDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'point')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 73, 6))
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
StringsDefinition._Automaton = _BuildAutomaton_3()




StringsModelDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'label'), pyxb.binding.datatypes.string, scope=StringsModelDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 81, 6)))

StringsModelDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=StringsModelDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 82, 6)))

StringsModelDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=StringsModelDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 83, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 81, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 82, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 83, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StringsModelDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'label')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 81, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StringsModelDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 82, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StringsModelDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 83, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StringsModelDefinition._Automaton = _BuildAutomaton_4()




StringsPointDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'label'), pyxb.binding.datatypes.string, scope=StringsPointDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 89, 6)))

StringsPointDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=StringsPointDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 90, 6)))

StringsPointDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=StringsPointDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 91, 6)))

StringsPointDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'symbol'), StringsSymbolDefinition, scope=StringsPointDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 92, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 89, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 90, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 91, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 92, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StringsPointDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'label')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 89, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StringsPointDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 90, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StringsPointDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 91, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(StringsPointDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'symbol')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 92, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StringsPointDefinition._Automaton = _BuildAutomaton_5()




StringsSymbolDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'label'), pyxb.binding.datatypes.string, scope=StringsSymbolDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 99, 6)))

StringsSymbolDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'description'), pyxb.binding.datatypes.string, scope=StringsSymbolDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 100, 6)))

StringsSymbolDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'notes'), pyxb.binding.datatypes.string, scope=StringsSymbolDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 101, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 99, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 100, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 101, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(StringsSymbolDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'label')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 99, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(StringsSymbolDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'description')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 100, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(StringsSymbolDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'notes')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 101, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
StringsSymbolDefinition._Automaton = _BuildAutomaton_6()




PointDefinition._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'symbol'), SymbolDefinition, scope=PointDefinition, location=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 50, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 50, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(PointDefinition._UseForTag(pyxb.namespace.ExpandedName(None, u'symbol')), pyxb.utils.utility.Location('/Users/brett/dev/gdwd/ped/plantextract/smdx.xsd', 50, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
PointDefinition._Automaton = _BuildAutomaton_7()

