import os
from flask import Flask

app = Flask('cdn')

@app.route('/ping')
def ping():
    return 'Pong'
