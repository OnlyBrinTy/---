from flask import Flask, render_template

app = Flask(__name__)


@app.route('/astronauts_selection', methods=['POST', 'GET'])
def do_thing():
    if request.method == 'GET':
        param = {}
        param['titlle'] = 'Форма'
        return render_template('selection.html', **param)
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
