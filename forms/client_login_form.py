from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ClientLoginForm(FlaskForm):
    login = StringField("Номер телефона", validators=[DataRequired()])
    submit = SubmitField("ПОЛУЧИТЬ КОД")
