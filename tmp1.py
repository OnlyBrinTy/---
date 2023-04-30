import sys
from io import BytesIO
import requests
from PIL import Image


def get_size(toponym):
    ''' возвращает размеры области объекта по его топониму'''
    spn_longitude1, spn_lattitude1 = toponym['boundedBy']['Envelope']['lowerCorner'].split(" ")
    spn_longitude2, spn_lattitude2 = toponym['boundedBy']['Envelope']['upperCorner'].split(" ")
    delta1 = str(float(spn_longitude2) - float(spn_longitude1))
    delta2 = str(float(spn_lattitude2) - float(spn_lattitude1))
    return delta1, delta2


def do_request(toponym_to_find=" ".join(sys.argv[1:])):
    '''запуск через командную строку python search.py Москва, ул. Ак. Королева, 12
    возвращает параметры для статик карты'''

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        # обработка ошибочной ситуации
        pass


    json_response = response.json()

    toponym = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    # Собираем параметры для запроса к StaticMapsAPI:
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(list(get_size(toponym))),
        "l": "map",
        "pt": f'{toponym_longitude},{toponym_lattitude},pm2vvl'
    }
    return map_params


def draw(map_params):
    """Создадим картинку и тут же ее покажем встроенным просмотрщиком операционной системы"""
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    # ... и выполняем запрос
    response = requests.get(map_api_server, params=map_params)

    Image.open(BytesIO(
        response.content)).show()
