from flask import Flask

app = Flask(__name__)


@app.route('/promotion_image')
def do_thing():
    with open('index.html', 'r', encoding='utf-8') as stream:
        return stream.read()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
