from flask import Flask, render_template

app = Flask(__name__)
crew = ('Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин')


@app.route('/')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/index/<title>')
def index1(title):
    return render_template('base.html', title1=title)


@app.route('/distribution')
def training():
    return render_template('auto_answer.html', title1='Анкета', crew=crew)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
