from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddressForm(FlaskForm):
    city = SelectField("Город*", validators=[DataRequired()], choices=[('Стерлитамак', 'Стерлитамак'), ('Кумертау', 'Кумертау')])
    street = StringField("Улица*", validators=[DataRequired()])
    house_number = StringField("Номер дома*", validators=[DataRequired()])
    flat = StringField("Квартира / офис*", validators=[DataRequired()])
    entrance = StringField("Подъезд")
    floor = StringField("Этаж")
    doorphone = StringField("Код домофона")

    submit = SubmitField("ПРИНЯТЬ")
