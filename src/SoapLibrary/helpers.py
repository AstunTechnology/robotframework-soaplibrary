import io
from collections import OrderedDict
from zeep import xsd, helpers
from lxml import etree

class HelperKeywords(object):

    def serialize_object(self, obj, target_cls=OrderedDict):
        return helpers.serialize_object(obj, target_cls)

    def create_xml_soap_map(self, values):
        return helpers.serialize_object(values)

    def guess_xsd_type(self, obj):
        return helpers.guess_xsd_type(obj)

    def Nil(self):
        return helpers.Nil()

    class ArrayOfStrings(list):

        def init(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    class ArrayOfAny(list):

        def init(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
