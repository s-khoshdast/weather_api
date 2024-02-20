from django.shortcuts import render
from django.core.cache import cache
from requests import HTTPError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .serializers import WeatherSerializer, WeatherAPIErrorSerializer
from api.services.city_data import validate_city_name
from api.services.errors import WeatherAPIError, WeatherAPIHTTPError, MissingCityError
from api.services.weather_data import fetch_weather_data
from api.services.data_loader import DataLoaderSingleton
# Create your views here.

@extend_schema(
    request=WeatherSerializer,
    responses={
        200: WeatherSerializer,
        400: WeatherAPIErrorSerializer,
        401: WeatherAPIErrorSerializer,
        404: WeatherAPIErrorSerializer,
        500: WeatherAPIErrorSerializer
    }

)

class WeatherView(APIView):

    def get(self, request, city_name=None):
        if not city_name or not validate_city_name(city_name):
            return MissingCityError().to_response()

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

            return WeatherAPIHTTPError(http_err).to_response()


