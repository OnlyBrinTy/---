from flask import Flask, render_template, request
import os

current_file_name = 'None'
IMG_PATH = 'static/img/'
app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def do_thing():
    global current_file_name

    if request.method == 'POST':
        image = request.files['file']
        current_file_name = image.filename
        image.save(os.path.join(IMG_PATH, image.filename))

    param = {'title': 'Отбор астронавтов', 'filename': IMG_PATH + current_file_name}
    return render_template('selection.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
