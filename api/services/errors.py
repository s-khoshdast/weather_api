from requests import HTTPError
from rest_framework.response import Response
from rest_framework import status
from api.serializers import WeatherAPIErrorSerializer


class WeatherAPIError():
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    serializer_class = WeatherAPIErrorSerializer

    def __init__(self, description):
        self.description = description or "Internal Server Error"
    
    def to_response(self):
        serialized_error = self.serializer_class(data={
            'code': self.code,
            'description': self.description,
            
        })
        serialized_error.is_valid(raise_exception=True)
        return Response(serialized_error.data, status=self.code)
    
class WeatherAPIHTTPError(WeatherAPIError):
    responseModel = 'HTTPError'
    def __init__(self, http_error : HTTPError):
        super().__init__(description=str(http_error.response.reason))
        self.code = http_error.response.status_code

class MissingCityError(WeatherAPIError):
    def __init__(self):
        super().__init__(description='missed or invalid city_name argument.')
        self.code = status.HTTP_400_BAD_REQUEST
        