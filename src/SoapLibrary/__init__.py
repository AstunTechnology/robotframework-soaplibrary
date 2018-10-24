from .version import VERSION
from .clientmanagement import ClientManagementKeywords
from .helpers import HelperKeywords

__version__ = VERSION

class SoapLibrary(ClientManagementKeywords, HelperKeywords):

    def __init__(self):
        self.client = None