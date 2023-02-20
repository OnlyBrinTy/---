from flask import Flask, render_template

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def do_thing(nickname, level, rating):
    params = {"title": 'Результаты', 'name': nickname, 'level': level, 'rating': rating}
    return render_template('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
