from django.shortcuts import render
from django.core.cache import cache
from requests import HTTPError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import WeatherSerializer, MissingOrIvalidCityErrorSerializer, CityNotFoundErrorSerializer, InternalServerErrorSerializer
from api.services.weather_data import fetch_weather_data
from api.services.data_loader import DataLoaderSingleton
# Create your views here.

@extend_schema(
    request=WeatherSerializer,
    responses={
        200: WeatherSerializer,
        400: MissingOrIvalidCityErrorSerializer,
        404: CityNotFoundErrorSerializer,
        500: InternalServerErrorSerializer,
    },
)
class WeatherView(APIView):

    def get(self, request, city_name=None):
        if not city_name:
            return Response({'error': 'Missing city_name parameter'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data_loader = DataLoaderSingleton()
            config = data_loader.config

            lang = config.get('lang')
            cache_time = config.get('cache_time')
            
            cache_key = f'{city_name}_{lang}'
            
            weather_data = cache.get(cache_key)
            if weather_data is not None:
                return Response(weather_data)
            
            data = fetch_weather_data(city_name, config)
            weather_serializer = WeatherSerializer(data)
            weather_data = weather_serializer.data
            cache.set(cache_key, weather_data, int(cache_time) * 60)

            return Response(weather_data, status=status.HTTP_200_OK)
        
        except HTTPError as http_err:

            ERROR_REASON = str(http_err.response.reason)
            ERROR_STATUS_CODE = http_err.response.status_code


            return Response({'error': ERROR_REASON}, status=ERROR_STATUS_CODE)

