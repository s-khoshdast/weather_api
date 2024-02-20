import re

def validate_city_name(city_name):
    
    pattern = r"^([a-zA-Z]+(?: [a-zA-Z]+)*)'?$"
    return bool(city_name and re.match(pattern, city_name))
