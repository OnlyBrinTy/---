from flask import Flask, render_template

PLANETS_FACTS = {'Марс': ['Находится недалеко от земли;', 'Имеет воду на полюсах;',
                          'Возможно обладает примитивной жизнью;', 'Разряженная атмосфера;',
                          'И имеет невероятный уровень радиации на поверхности!'],
                 'Земля': ['Это наша родная планета;', 'Большая часть поверхности покрыта водой;',
                           'Обитаема самыми разными животными;', 'Атмосфера насыщенна кислородом;',
                           'И пришельцы очень удивятся, когда они приедут к нам!']}
app = Flask(__name__)


@app.route('/choice/<planet>')
def do_thing(planet):
    params = {"title": 'Варианты выбора',  "planet": planet, 'facts': PLANETS_FACTS.get(planet, ['No info'] * 5)}
    return render_template('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
