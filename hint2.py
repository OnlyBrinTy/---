from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    with open('p.json', 'r', encoding='utf-8') as inp_file:
        return inp_file.read()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


import json
from argparse import ArgumentParser
import requests

parser = ArgumentParser()
parser.add_argument('host', type=str, nargs='?')
parser.add_argument('port', type=int, nargs='?')
parser.add_argument('color', type=str, nargs='?')
parser.add_argument('-shadow', '--shadow', type=int, default=0)

args = parser.parse_args()

address = f'http://{args.host}:{args.port}'

result = requests.get(address)
jsn = result.json()

with open('m.json', 'w', encoding='utf-8') as out_file:
    dict_file = jsn
    res = {}
    for key, val in dict_file.items():
        plants = [(v['name'], v['shadow']) for v in val]
        plants.sort(key=lambda t: t[1])

        if len(set(list(zip(*plants))[1])) == 1:
            plants.sort(key=lambda t: t[0])

        res[key] = [p[0] for p in plants]

    json.dump(res, out_file)
