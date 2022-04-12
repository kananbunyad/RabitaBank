from flask import render_template
from app import app
from models import *
from flask import request
from forms import CardOrderForm,SavingsOrderForm
from upload import save_file



@app.route("/kampaniyalar")
def kampaniyalar():
    kampcard = Kampaniyalar.query.all()
    return render_template('kampaniyalar.html', kampcard=kampcard)

@app.route('/universal-emanet/<int:card_id>')
def emanetlerid(card_id):
    kart = Card.query.all()
    payment = PaymentFrequency.query.all()
    cancel = Cancellation.query.all()
    card_id -= 1
    kart = kart[card_id]
    payment = payment[card_id]
    print(payment)
    cancel = cancel[card_id]
    kampcard = Kampaniyalar.query.all()
    return render_template('emanetlerdaxili.html', kampcard=kampcard,kart=kart,payment=payment,cancel=cancel)

# @app.route("/universal-emanet")
# def emanetlerdaxili():
#     kampcard = Kampaniyalar.query.all()
#     return render_template('emanetlerdaxili.html', kampcard=kampcard)

@app.route("/ferdi-emanetler", methods = ['GET', 'POST'])
def ferdiemanetler():
    post_data1 = request.form
    form = SavingsOrderForm()
    card = Card.query.all()
    if request.method == 'POST':
        form = SavingsOrderForm(data=post_data1)
        if form.validate_on_submit():
            contact = SavingsOrder(name = form.name.data, surname = form.surname.data, savings = form.saving_choice.data, phone_number = form.phone_number.data)
            contact.save()
    return render_template('ferdiemanetler.html', cards=card, form=form)

@app.route("/kartsifarishi", methods = ['GET', 'POST'])
def index():
    post_data = request.form
    form = CardOrderForm()
    if request.method == 'POST':
            form = CardOrderForm(data=post_data)
            # photo1 = save_file(form.document1.data)
            # photo2 = save_file(form.document2.data)
            if form.validate_on_submit():
                contact = CardOrder(card_choise = form.card_choise.data, select_card = form.select_card.data, currency = form.currency.data, term = form.term.data, main_office = form.main_office.data, phone_number = form.phone_number.data, document1 = form.document1.data, document2 = form.document2.data, email = form.email.data)
                contact.save()
    return render_template('kartsifarishi.html', form=form)