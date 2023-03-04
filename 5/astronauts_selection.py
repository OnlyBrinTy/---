from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/astronauts_selection', methods=['POST', 'GET'])
def do_thing():
    if request.method == 'GET':
        param = {}
        param['title'] = 'Отбор астронавтов'
        return render_template('selection.html', **param)
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['about'])

        return "<h1>Форма отправлена</h1>"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
