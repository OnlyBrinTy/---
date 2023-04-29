from flask_wtf import *
from wtforms import *
from wtforms.validators import *


class EditPhoto(FlaskForm):
    change_avatar = FileField('Выбрать', validators=[DataRequired()])

    submit_avatar = SubmitField('Изменить')
