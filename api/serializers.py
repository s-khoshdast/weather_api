from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    city_name = serializers.CharField(max_length=255, source='name')
    temp_current = serializers.FloatField(source='main.temp')
    temp_min = serializers.FloatField(source='main.temp_min')
    temp_max = serializers.FloatField(source='main.temp_max')
    humidity = serializers.IntegerField(source='main.humidity')
    pressure = serializers.IntegerField(source='main.pressure')
    wind_speed = serializers.FloatField(source='wind.speed')
    wind_direction = serializers.SerializerMethodField(method_name='get_wind_direction')
    description = serializers.SerializerMethodField(method_name='get_weather_description')

    def get_wind_direction(self, obj):
        directions = [
            'North',
            'Northeast',
            'East',
            'Southeast',
            'South',
            'Southwest',
            'West',
            'Northwest'
        ]
        
        index = int((obj['wind']['deg'] % 360.0) / 45.0)
        return directions[index]
    
    def get_weather_description(self, obj):
        weather_data = obj.get('weather')[0]
        try:
            return weather_data.get('description', 'N/A')
        except Exception as e:
            raise e