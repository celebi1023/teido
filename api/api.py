import requests
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from extract import handlePDF, handleEPUB
from analyze import analyzeText

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

def allowed_file(filename):
    if '.' not in filename or \
           filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
           return 'invalid'
    return filename.rsplit('.', 1)[1].lower()

@app.route('/reg', methods=['POST'])
def upload_file():
    print('IN TEST')
    print(request)
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(file.filename)
        print(type(file))
        print(file.content_type)

        data = {}
        if file.content_type == 'application/pdf':
            data = handlePDF(filename)

        elif file.content_type == 'application/epub+zip':
            data = handleEPUB(filename)

        os.remove('files/' + filename)
        print(data)
    return data