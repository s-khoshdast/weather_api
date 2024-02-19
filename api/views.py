from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.services.weather_data import fetch_weather_data

# Create your views here.

class WeatherView(APIView):

    def get(self, request, city_name):
        if not city_name:
            return Response({'error': 'Missing city_name parameter'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = fetch_weather_data(city_name)
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

