from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app
from models import Card, Kampaniyalar,db,CardOrder,SavingsOrder,PaymentFrequency,Cancellation


admin = Admin(app, name='RabitaBank', template_mode='bootstrap4')



admin.add_view(ModelView(Card, db.session))
admin.add_view(ModelView(Kampaniyalar, db.session))
admin.add_view(ModelView(CardOrder, db.session))
admin.add_view(ModelView(SavingsOrder, db.session))
admin.add_view(ModelView(PaymentFrequency, db.session))
admin.add_view(ModelView(Cancellation, db.session))