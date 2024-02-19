from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

class WeatherSerializer(serializers.Serializer):
    city_name = serializers.CharField(max_length=255, source='name', label=_('City Name'))
    temp_current = serializers.FloatField(source='main.temp', label=_("Current Temperature"))
    temp_min = serializers.FloatField(source='main.temp_min', label=_("Minimum Temperature"))
    temp_max = serializers.FloatField(source='main.temp_max', label=_("Maximum Temperature"))
    humidity = serializers.IntegerField(source='main.humidity', label=_("Humidity"))
    pressure = serializers.IntegerField(source='main.pressure', label=_('Pressure'))
    wind_speed = serializers.FloatField(source='wind.speed', label=_("Wind Speed"))
    wind_direction = serializers.SerializerMethodField(method_name='get_wind_direction', label=_("Wind Direction"))
    description = serializers.SerializerMethodField(method_name='get_weather_description', label=_("Descriptin"))

    def get_wind_direction(self, obj):
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
    
    def get_weather_description(self, obj):
        weather_data = obj.get('weather')[0]
        try:
            return weather_data.get('description', 'N/A')
        except Exception as e:
            raise e