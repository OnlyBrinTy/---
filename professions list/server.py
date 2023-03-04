from flask import Flask, render_template

app = Flask(__name__)
professions = ('инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач', 'инженер по терраформированию',
               'климатолог', 'специалист по радиационной защите', 'астрогеолог', 'гляциолог', 'пилот дронов',
               'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер', 'штурман')


@app.route('/')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/index/<title>')
def index1(title):
    return render_template('base.html', title1=title)


@app.route('/list_prof/<list_type>')
def training(list_type):
    return render_template('training.html', title1='training', profs=professions, list_type=list_type)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
