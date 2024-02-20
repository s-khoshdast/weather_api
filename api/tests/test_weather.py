import pytest
from django.urls import reverse
from rest_framework import status
from api.services.errors import MissingCityError, WeatherAPIError

@pytest.fixture
def get_city_request(client):
    def do_get_city_request(city_name):
        url = reverse('weather-view', kwargs={'city_name' : city_name})
        return client.get(url)
    return do_get_city_request

@pytest.mark.django_db
class TestWeatherAPI:

    def test_if_city_is_missed_returns_400(self, client):
        
        response = client.get('/api/weather/', {'city_name' : ''})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_if_city_is_invalid_returns_400(self, client, get_city_request):
        response = get_city_request('<London>')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_city_is_not_found_returns_404(self, client, get_city_request):
        response = get_city_request('a')

        assert response.status_code == status.HTTP_404_NOT_FOUND
        
    def test_if_city_is_valid_returns_200(self, client, get_city_request):
        response = get_city_request('London')

        assert response.status_code == status.HTTP_200_OK

    