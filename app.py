from flask import Flask
import os
app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/RabitaBank'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



BASE_DIRS = os.path.dirname(os.path.abspath(__file__))

UPLOADED_FILES_DIR = os.path.join(BASE_DIRS, 'media')
app.config['UPLOAD_FOLDER'] = UPLOADED_FILES_DIR
if not os.path.isdir(UPLOADED_FILES_DIR):
    os.mkdir(UPLOADED_FILES_DIR)

from extensions import *
from controllers import *
from models import *
from admin import *

if __name__==("__main__"):
    app.init_app(db)
    app.init_app(migrate)
    app.run(port=5000, debug=True)

