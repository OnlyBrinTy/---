from tmp1 import do_request, draw
import requests


map_params = do_request()

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"


search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": map_params['ll'],
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
if not response:
    pass

# Преобразуем ответ в json-объект
json_response = response.json()


labels = []
for feature in json_response["features"]:
    if feature['properties']['CompanyMetaData']['Categories'][0]['name'] == 'Аптека':
        cords = ','.join(map(str, feature['geometry']['coordinates']))

        hours = feature['properties']['CompanyMetaData'].get('Hours')
        if hours:
            if 'круглосуточн' in hours['text']:
                labels.append(f"{cords},pm2dgl")
            else:
                labels.append(f"{cords},pm2bll")
        else:
            labels.append(f"{cords},pm2grl")


delta = "0.04"

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    # позиционируем карту центром на наш исходный адрес
    "ll": map_params['ll'],
    "spn": ",".join([delta, delta]),
    "l": "map",
    # добавим точку, чтобы указать найденную аптеку
    "pt": '~'.join(labels)
}

draw(map_params)
