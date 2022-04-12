from secrets import choice
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired

card_debet = ["Karti secin", "Kartmane Debet"]
term_choise = ["Kartin muddeti", "5 il"]
card_type = ["Kart novu secin","MasterCard", "Visa" ]
branchs = ["Bash Ofis", "Nesimi filiali", "Buta filiali", "Kaspian filiali", "Masalli filiali", "Qaradağ filialı"]
radio_choice = ["AZN", "USD", "EUR"]
saving_choices = ["Emanet novunu sech", "Universal emanetler", "Ushag yigim emaneti", "Saxlanc emaneti"]


class CardOrderForm(FlaskForm):
    card_choise = SelectField(label = 'Kartmane', choices = card_debet)
    select_card = SelectField(label='Kart Növü', choices=card_type)
    currency = SelectField(label="Valyuta", choices = radio_choice)
    term = SelectField(label="Müddət", choices = term_choise)
    main_office = SelectField(label='Filiali sec', choices = branchs)
    phone_number = StringField(label='Mobil nömrəniz:', validators=[Length(max=20)])
    document1 = FileField(label="")
    document2 = FileField(label="")
    email = StringField(label='Elektron poçtunuz:', validators=[Length(max=30)])


class SavingsOrderForm(FlaskForm):
    name = StringField(label='Adınız:',validators=[Length(max=100)])
    surname = StringField(label='Soyadınız:', validators=[Length(max=100)])
    saving_choice = SelectField(label = 'Əmanət növünü seçin', choices = saving_choices)
    phone_number = StringField(label='Mobil nömrəniz:',validators=[Length(max=20)])


