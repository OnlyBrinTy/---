from flask import Flask, render_template
from werkzeug.utils import secure_filename
from form import EditPhoto

app = Flask('foo')
app.config['SECRET_KEY'] = 'secret'

images = ['6_venus_lightning_concept_2006_h.webp.crdownload',
          '1645567084_1-gamerwall-pro-p-planeta-venera-vid-s-zemli-krasivie-oboi-1.jpeg',
          'shitovoy-vulkan.jpeg']


@app.route('/carousel', methods=['GET', 'POST'])
def do_thing():
    global images
    form = EditPhoto()

    if form.validate_on_submit():
        filename = secure_filename(form.change_avatar.data.filename)
        form.change_avatar.data.save('static/img/' + filename)

        images.insert(0, filename)
        del images[-1]

    param = {'title': 'Пейзажи Венеры',
             'form': form,
             'imgs': images}

    return render_template('selection.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
