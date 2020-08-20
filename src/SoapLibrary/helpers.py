from collections import OrderedDict
from zeep import xsd, helpers

class HelperKeywords(object):

    def serialize_object(self, obj, target_cls=OrderedDict):
        return helpers.serialize_object(obj, target_cls)

    def create_xml_soap_map(self, values):
        return helpers.serialize_object(values)

    def guess_xsd_type(self, obj):
        return helpers.guess_xsd_type(obj)

    def Nil(self):
        return helpers.Nil()

    def convert_to_anytype_list(self, value):
        result = [ ]
        for item in value:
            result.append(self.convert_to_anytype(item))
        return result

    def convert_to_string_list(self, value):
        result = [ ]
        for item in value:
            result.append(self.convert_to_string(item))
        return result

    def convert_to_anytype(self, value):
        return xsd.AnyObject(xsd.String(), value)

    def convert_to_string(self, value):
        return xsd.String(value)