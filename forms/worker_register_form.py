from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField


class WorkerRegisterForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    surname = StringField("Фамилия", validators=[DataRequired()])
    phone_number = StringField("Номер телефона", validators=[DataRequired()])
    email =  EmailField("E-mail", validators=[DataRequired()])
    birthday = StringField("День рождения", validators=[DataRequired()])
    address = StringField("Адрес работы", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])

    submit = SubmitField("ЗАРЕГИСТРИРОВАТЬ")
