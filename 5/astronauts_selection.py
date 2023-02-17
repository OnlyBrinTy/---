from flask import Flask, render_template

app = Flask(__name__)


@app.route('/astronauts_selection', methods=['POST', 'GET'])
def do_thing():
    param = {}
    param['titlle'] = 'рварвар'
    return render_template('selection.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
