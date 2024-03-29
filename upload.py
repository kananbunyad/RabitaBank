from flask import url_for
from app import UPLOADED_FILES_DIR, os
from werkzeug.utils import secure_filename

def save_file(f):

    filename = secure_filename(f.filename)
    file_dir = os.path.join(UPLOADED_FILES_DIR, filename)
    f.save(file_dir)
    file_path = url_for('uploaded_file', filename=filename)
    return file_path


