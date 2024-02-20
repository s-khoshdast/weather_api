from django.urls import path
from .views import WeatherView

# URLConf
urlpatterns = [
    path('weather/', WeatherView.as_view(), name='weather_missing_city'),
    path('weather/<str:city_name>/', WeatherView.as_view(), name='weather-view')
]