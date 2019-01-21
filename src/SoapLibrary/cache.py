from zeep.cache import InMemoryCache
import os, logging

class InMemoryCachePreloader(InMemoryCache):
    """A preloader for the InMemoryCache which will load
    the files from the supplied path merged with the
    supplied base_path and add them to the InMemoryCache

    usage:
        cache = InMemoryCachePreloader(os.path.join(os.getcwd(), 'schemas/'))
        cache.add_file('http://schemas.xmlsoap.org/soap/encoding/', 'schemas.xmlsoap.org/soap/encoding.xsd')
    """

    def __init__(self, base_path):
        logging.info('Creating cache {0}'.format(base_path))
        self.base_path = base_path
        super().__init__()
    
    def add_file(self, url, path):
        full_path = os.path.join(self. base_path, path)
        logging.info('Adding cache item {0} at {1}'.format(url, full_path))
        content = self._load_from_disk(full_path)
        if content is None:
            logging.info('Unable to cache file {0}'.format(full_path))
        else:
            super().add(url, content)

    def _load_from_disk(self, path):
        try:
            with open(path, 'r') as f:
                return f.read().encode('utf-8')
        except:
            return None

    def get(self, url):
        content = super().get(url)
        if content is not None:
            logging.info('Cache HIT for {0}'.format(url))
        else:
            logging.info('Cache MISS for {0}'.format(url))

        return content
