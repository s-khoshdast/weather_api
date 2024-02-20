import os
import yaml
from django.conf import settings

def validate_config(config_file):
    valid_langs = ["en", "de", "fr"]
    valid_cache_times = [5, 10, 60]

    with open(config_file, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    try: 
        # Load API key from apikey.yaml in the same directory as config_file
        apikey_file = os.path.join(os.path.dirname(config_file), "apikey.yaml")
        with open(apikey_file, 'r') as f:
            api_key_data = yaml.load(f, Loader=yaml.FullLoader)

        config['api_key'] = api_key_data['api_key']  # Assuming apikey.yaml contains a key named 'api_key'

    except Exception as e:
        raise e

    if config['lang'] not in valid_langs:
        raise ValueError("Invalid language specified in configuration")

    if config['cache_time'] not in valid_cache_times:
        raise ValueError("Invalid cache time specified in configuration")

    return config

class DataLoaderSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = None
            cls._instance.load_data()
        return cls._instance
    
    def load_data(self):
            self._config = validate_config(settings.API_CONFIG_FILE)
        
    @property
    def config(self):
        return self._config