from flask import render_template 
from . import pitch

@pitch.route('/')
def home():
    return render_template('index.html')