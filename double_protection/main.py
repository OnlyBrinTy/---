import os
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

my_secret = os.environ['KEY']
app = Flask(__name__)
app.config['SECRET_KEY'] = my_secret


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/success', methods=['GET', 'POST'])
def success():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('success.html', title='Успешно', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
