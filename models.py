from unicodedata import category
from extensions import db 

class Card(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    term = db.Column(db.String(255), nullable=True)
    interest_rate = db.Column(db.String(255), nullable=True)
    imgsrc = db.Column(db.String(255), nullable=False)


    def __repr__(self):
        return self.title


    def __init__(self, title, term=None, interest_rate=None, imgsrc=None):
        self.title = title
        self.term = term
        self.interest_rate = interest_rate
        self.imgsrc = imgsrc


    def save(self):
        db.session.add(self)
        db.session.commit()   




class Kampaniyalar(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    imgsrc = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(255), nullable=False)




    def __repr__(self):
        return self.title


    def __init__(self, title, description=None, imgsrc=None, category=None):
        self.title = title
        self.description = description
        self.imgsrc = imgsrc
        self.category = category


    def save(self):
        db.session.add(self)
        db.session.commit()   



class CardOrder(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    card_choise = db.Column(db.String(100), nullable=False)
    select_card = db.Column(db.String(100), nullable=False)
    currency = db.Column(db.String(100), nullable=False)
    term = db.Column(db.String(30),nullable=False)
    main_office = db.Column(db.String(30),nullable=False)
    document1 = db.Column(db.String(30),nullable=False)
    document2 = db.Column(db.String(30),nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30),nullable=False)

    def _repr_(self):
        return self.main_office

    def _init_(self,card_choise , select_card, currency, term, main_office, phone_number, document1, document2, email):
        self.card_choise=card_choise
        self.select_card=select_card
        self.currency=currency
        self.term = term
        self.main_office = main_office
        self.phone_number=phone_number
        self.document1=document1
        self.document2=document2
        self.email = email

    def save(self):
        db.session.add(self)
        db.session.commit()



class PaymentFrequency(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    teleb1 = db.Column(db.String(100), nullable=False)
    teleb2 = db.Column(db.String(100), nullable=False)
    teleb3 = db.Column(db.String(100), nullable=False)
    threemonth1 = db.Column(db.String(100), nullable=False)
    threemonth2 = db.Column(db.String(100), nullable=False)
    threemonth3 = db.Column(db.String(100), nullable=False)
    sixmonth1 = db.Column(db.String(100), nullable=False)
    sixmonth2 = db.Column(db.String(100), nullable=False)
    sixmonth3 = db.Column(db.String(100), nullable=False)
    twelvemonth1 = db.Column(db.String(100), nullable=False)
    twelvemonth2 = db.Column(db.String(100), nullable=False)
    twelvemonth3 = db.Column(db.String(100), nullable=False)
    twenty4month1 = db.Column(db.String(100), nullable=False)
    twenty4month2 = db.Column(db.String(100), nullable=False)
    twenty4month3 = db.Column(db.String(100), nullable=False)
    thirty6month1 = db.Column(db.String(100), nullable=False)
    thirty6month2 = db.Column(db.String(100), nullable=False)
    thirty6month3 = db.Column(db.String(100), nullable=False)


    def _repr_(self):
        return self.teleb1

    def _init_(self,teleb1 ,teleb2, teleb3, threemonth1, threemonth2, threemonth3, sixmonth1, sixmonth2, sixmonth3, twelvemonth1, twelvemonth2, twelvemonth3, twenty4month1, twenty4month2,twenty4month3, thirty6month1, thirty6month2, thirty6month3):
        self.teleb1=teleb1
        self.teleb2=teleb2
        self.teleb3=teleb3
        self.threemonth1=threemonth1
        self.threemonth2=threemonth2
        self.threemonth3=threemonth3
        self.sixmonth1=sixmonth1
        self.sixmonth2=sixmonth2
        self.sixmonth3=sixmonth3
        self.twelvemonth1=twelvemonth1
        self.twelvemonth2=twelvemonth2
        self.twelvemonth3=twelvemonth3
        self.twenty4month1=twenty4month1
        self.twenty4month2=twenty4month2
        self.twenty4month3=twenty4month3
        self.thirty6month1=thirty6month1
        self.thirty6month2=thirty6month2
        self.thirty6month3=thirty6month3


    def save(self):
        db.session.add(self)
        db.session.commit()

class Cancellation(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    till30_1 = db.Column(db.String(100), nullable=False)
    till30_2 = db.Column(db.String(100), nullable=False)
    till30_3 = db.Column(db.String(100), nullable=False)
    till180_1 = db.Column(db.String(100), nullable=False)
    till180_2 = db.Column(db.String(100), nullable=False)
    till180_3 = db.Column(db.String(100), nullable=False)
    till360_1 = db.Column(db.String(100), nullable=False)
    till360_2 = db.Column(db.String(100), nullable=False)
    till360_3 = db.Column(db.String(100), nullable=False)
    after360_1 = db.Column(db.String(100), nullable=False)
    after360_2 = db.Column(db.String(100), nullable=False)
    after360_3 = db.Column(db.String(100), nullable=False)



    def _repr_(self):
        return self.till30_1

    def _init_(self,till30_1 ,till30_2, till30_3, till180_1, till180_2, till180_3, till360_1, till360_2, till360_3, after360_1, after360_2, after360_3):
        self.till30_1=till30_1
        self.till30_2=till30_2
        self.till30_3=till30_3
        self.till180_1=till180_1
        self.till180_2=till180_2
        self.till180_3=till180_3
        self.till360_1=till360_1
        self.till360_2=till360_2
        self.till360_3=till360_3
        self.after360_1=after360_1
        self.after360_2=after360_2
        self.after360_3=after360_3



    def save(self):
        db.session.add(self)
        db.session.commit()

class SavingsOrder(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    savings = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)


    def _repr_(self):
        return self.name

    def _init_(self,name , surname, savings, phone_number):
        self.name=name
        self.surname=surname
        self.savings=savings
        self.phone_number=phone_number


    def save(self):
        db.session.add(self)
        db.session.commit()

