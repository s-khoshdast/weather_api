from django.shortcuts import render
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import WeatherSerializer
from api.services.weather_data import fetch_weather_data
from api.services.data_loader import DataLoaderSingleton
# Create your views here.

class WeatherView(APIView):

    def get(self, request, city_name):
        if not city_name:
            return Response({'error': 'Missing city_name parameter'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data_loader = DataLoaderSingleton()
            config = data_loader.config
            data = fetch_weather_data(city_name, config)
            weather_serializer = WeatherSerializer(data)
            return Response(weather_serializer.data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

