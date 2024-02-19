from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class WeatherSerializer(serializers.Serializer):
    cityName = serializers.CharField(max_length=255, source='name', label=_('City Name'))
    tempCurrent = serializers.FloatField(source='main.temp', label=_("Current Temperature"))
    tempMin = serializers.FloatField(source='main.temp_min', label=_("Minimum Temperature"))
    tempMax = serializers.FloatField(source='main.temp_max', label=_("Maximum Temperature"))
    humidity = serializers.IntegerField(source='main.humidity', label=_("Humidity"))
    pressure = serializers.IntegerField(source='main.pressure', label=_('Pressure'))
    windSpeed = serializers.FloatField(source='wind.speed', label=_("Wind Speed"))
    windDirection = serializers.SerializerMethodField(method_name='get_wind_direction', label=_("Wind Direction"))
    description = serializers.SerializerMethodField(method_name='get_weather_description', label=_("Descriptin"))

    def get_wind_direction(self, obj) -> str:
        directions = [
            _('North'),
            _('Northeast'),
            _('East'),
            _('Southeast'),
            _('South'),
            _('Southwest'),
            _('West'),
            _('Northwest')
        ]
        
        index = int((obj['wind']['deg'] % 360.0) / 45.0)
        return directions[index]
    
    def get_weather_description(self, obj) -> str:
        weather_data = obj.get('weather')[0]
        try:
            return weather_data.get('description', 'N/A')
        except Exception as e:
            raise e

class MissingOrIvalidCityErrorSerializer(serializers.Serializer):
    statusCode = serializers.IntegerField()
    message = serializers.CharField(max_length=255)
class CityNotFoundErrorSerializer(serializers.Serializer):
    statusCode = serializers.IntegerField()
    message = serializers.CharField(max_length=255)

class InternalServerErrorSerializer(serializers.Serializer):
    statusCode = serializers.IntegerField()
    message = serializers.CharField(max_length=255)