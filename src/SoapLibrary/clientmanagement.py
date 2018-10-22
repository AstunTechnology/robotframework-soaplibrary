from zeep import Client
from zeep.plugins import HistoryPlugin
from zeep.settings import Settings
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth, HTTPProxyAuth, HTTPDigestAuth


class ClientManagementKeywords(object):

    def create_soap_client(self, url_or_path, timeout=90, username=None, password=None, auth_type='NONE', settings={}):
        url = url_or_path

        transport = Transport(timeout=timeout)
        if auth_type != 'NONE':
            session = Session()
            if auth_type == 'BASIC':
                session.auth = HTTPBasicAuth(username, password)
            elif auth_type == 'PROXY':
                session.auth = HTTPProxyAuth(username, password)
            elif auth_type == 'DIGEST':
                session.auth = HTTPDigestAuth(username, password)
            transport = Transport(session=session, timeout=timeout)

        client_settings = Settings()
        if len(settings) > 0:
            available_settings = ['strict', 'raw_response', 'forbid_dtd', 'forbid_entities', 'forbid_external', 'xml_huge_tree', 'force_https', 'extra_http_headers']
            for key in settings:
                if key in available_settings:
                    if key == 'strict':
                        client_settings.strict = settings[key]
                    elif key == 'raw_response':
                        client_settings.raw_response = settings[key]
                    elif key == 'forbid_dtd':
                        client_settings.forbid_dtd = settings[key]
                    elif key == 'forbid_entities':
                        client_settings.forbid_entities = settings[key]
                    elif key == 'forbid_external':
                        client_settings.forbid_external = settings[key]
                    elif key == 'xml_huge_tree':
                        client_settings.xml_huge_tree = settings[key]
                    elif key == 'force_https':
                        client_settings.force_https = settings[key]
                    elif key == 'extra_http_headers':
                        client_settings.extra_http_headers = settings[key]

        self.client = Client(url, transport=transport, plugins=[HistoryPlugin()], settings=client_settings)

        return self.client

    def call_soap_method(self, method, params=[]):
        return self.client.service[method](*params)

    def get_auth_type(self):
        if self.client.transport.session.auth is None:
            return 'NONE'
        elif type(self.client.transport.session.auth) is HTTPBasicAuth:
            return 'BASIC'
        elif type(self.client.transport.session.auth) is HTTPProxyAuth:
            return 'PROXY'
        elif type(self.client.transport.session.auth) is  HTTPDigestAuth:
            return 'DIGEST'
        else:
            return 'UNKNOWN'