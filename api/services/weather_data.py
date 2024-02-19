from django.conf import settings
import requests
import yaml

def fetch_weather_data(city_name, config):
    try:
        
        api_url = config.get('api_url', '')
        params = {
            'q': city_name,
            'appid': config.get('api_key', ''),
            'units': config.get('units', 'metric'),
            'lang': config.get('lang', 'en')
        }

        response = requests.get(api_url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        raise e