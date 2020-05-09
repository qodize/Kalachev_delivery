from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.fields.html5 import EmailField


class ClientForm(FlaskForm):
    name = StringField("Имя")
    surname = StringField("Фамилия")
    email = EmailField('E-mail')
    day = SelectField("День", choices=[(f"{x}", x) for x in range(1, 32)])
    month = SelectField("Месяц", choices=[('01', 'Январь'),
                                          ('02', 'Февраль'), ('03', 'Март'),
                                          ('04', 'Апрель'), ('05', 'Май'),
                                          ('06', 'Июнь'), ('07', 'Июль'),
                                          ('08', 'Август'), ('09', 'Сентябрь'),
                                          ('10', 'Октябрь'), ('11', 'Ноябрь'),
                                          ('12', 'Декабрь')])
    year = SelectField("Год", choices=[(f"{x}", x) for x in range(1969, 2021)])
    submit = SubmitField("СОХРАНИТЬ ИЗМЕНЕНИЯ")
