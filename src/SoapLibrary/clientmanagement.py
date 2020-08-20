from zeep import Client, xsd, helpers
from zeep.plugins import HistoryPlugin
from zeep.settings import Settings
from zeep.transports import Transport
from zeep.cache import InMemoryCache
from requests import Session
from requests.auth import HTTPBasicAuth, HTTPProxyAuth, HTTPDigestAuth
from .cache import InMemoryCachePreloader

class ClientManagementKeywords(object):

    def create_soap_client(self, url_or_path, timeout=90, username=None, password=None, auth_type='NONE', settings={}, cache=None):
        """Creates a Soap client using the zeep library

        -----

        Param

        *url_or_path :: string*

            The URL or path to the webservice. The client can read either a
            remote webservice or a local file from the OS

        -----

        Param

        *timeout :: integer [90]*

            The number of seconds before the request to the webservice times
            out

        -----

        Param

        *username :: string [None]*

            The username used for authenticating against webservices. If this
            is set, then the auth_type must also be set to something other
            than None

        -----

        Param

        *password :: string [None]*

            The password used for authenticating against webservices

        -----

        Param

        *auth_type :: string ["NONE"]*

            The authentication type to use when communicating with
            the webservice. Options are NONE, BASIC, PROXY and DIGEST. Any
            other than None requires that credentials also be supplied

        -----

        Param

        *Settings :: dict [Empty]*

            The settings allows the user to specify various settings to
            use when communicating with the webservice. They are detailed
            here: https://python-zeep.readthedocs.io/en/master/settings.html

        -----

        Return

        *Client*

            The client used for communicating with the webservice

        -----

        | A simple example |
        |                  | ${client}= | Create Soap Client | http://some-web-url.com/webservice?wsdl |
        |                  | ${answer}= | Call Soap Method | ${client} | getTheAnswer |

        | Settings example |
        |                   | &{settings}= | Create Dictionary | strict=False | raw_response=True |
        |                   | ${client}= |  Create Soap Client | http://some-web-url.com/webservice?wsdl | settings=&{settings} |
        |                   | ${answer}= | Call Soap Method | ${client} | getTheAnswer |

        | Basic authentication example |
        |                  | ${client}= |  Create Soap Client | http://some-web-url.com/webservice?wsdl | username=bob | password=bobspassword | auth_type=BASIC |
        |                  | ${answer}= | Call Soap Method | ${client} | getTheAnswer |

        """


        url = url_or_path

        transport = Transport(timeout=timeout, cache=cache)
        if auth_type != 'NONE':
            session = Session()
            if auth_type == 'BASIC':
                session.auth = HTTPBasicAuth(username, password)
            elif auth_type == 'PROXY':
                session.auth = HTTPProxyAuth(username, password)
            elif auth_type == 'DIGEST':
                session.auth = HTTPDigestAuth(username, password)
            transport = Transport(session=session, timeout=timeout, cache=cache)

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

        client = Client(url, transport=transport, plugins=[HistoryPlugin()], settings=client_settings)

        return client

    def call_soap_method(self, client, method, params={}):
        """Calls a method on the connected webservice

        -----

        Param

        *client : Zeep Client*

            The Client returned from the Create Soap Client method

        -----

        Param

        *method : string*

            The name of the method to call

        ------

        Param

        *params : list [Empty]*

            A list of parameters to pass to the method which must
            be specified in the order that the webservice is
            expecting them

        ------

        Return

        *result*

            An object determined to be the result of the call to
            the webservice

        ------

        | A simple example |
        |                  | Create Soap Client | http://some-web-url.com/webservice?wsdl |
        |                  | ${answer}= | Call Soap Method | getTheAnswer |

        """


        print("Parameters: {0}".format(params))
        return client.service[method](**params)

    def get_auth_type(self, client):
        """A utility keyword to determine which authentication is
        set in the current client

        -----

        Param

        *client : Zeep Client*

            The Client returned from the Create Soap Client method

        -----

        Return

        *auth_type*

            Either NONE, BASiC, PROXY, DIGEST or UNKNOWN

        -----

        | Basic authentication example |
        |                  | Create Soap Client | http://some-web-url.com/webservice?wsdl | username=bob | password=bobspassword | auth_type=BASIC |
        |                  | ${auth_type}= | Get Auth Type |

        """


        if client.transport.session.auth is None:
            return 'NONE'
        elif type(client.transport.session.auth) is HTTPBasicAuth:
            return 'BASIC'
        elif type(client.transport.session.auth) is HTTPProxyAuth:
            return 'PROXY'
        elif type(client.transport.session.auth) is  HTTPDigestAuth:
            return 'DIGEST'
        else:
            return 'UNKNOWN'

    def create_cache_preloader(self, base_path):
        """Returns an instance of the InMemoryCachePreloader"""
        return InMemoryCachePreloader(base_path)