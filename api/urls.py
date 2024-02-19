from django.urls import path
from .views import WeatherView

# URLConf
urlpatterns = [
    path('<str:city_name>/', WeatherView.as_view())
]