import yaml
from django.conf import settings

class DataLoaderSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = None
            cls._instance.load_data()
        return cls._instance
    
    def load_data(self):
        with open(settings.API_CONFIG_FILE, 'r') as f:
            self._config = yaml.load(f, Loader=yaml.FullLoader)
        
    @property
    def config(self):
        return self._config