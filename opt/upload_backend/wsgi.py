# This backend only will move the file from the nginx storage path to the path
# we choosed to keep the files (STORAGE_PATH).
import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# This variable is needed by the default gunicorn configuration
application = app

STORAGE_PATH = '/var/local/storage'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    os.rename(request.form['file.path'],
        os.path.join(STORAGE_PATH, request.form['file.name']))
    return 'You are done, the file is available <a href="/storage/">here</a>.'

if __name__ == '__main__':
    app.run()
