from flask import Flask, render_template
from config import config_options
from app import app



def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .main import pitch
    app.register_blueprint(pitch)
    return app

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)
