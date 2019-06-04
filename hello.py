from flask import Flask, make_response, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form

from wtforms import StringField, SubmitField
from wtforms.validators import Required

from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Alana Adelino e Silva'

moment = Moment(app)
manager = Manager(app)
bootstrap = Bootstrap(app)

class NameForm(Form):
    name = StringField('Name: ', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', current_time = datetime.utcnow(), form=form, name=name)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/response')
def responses():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html')

if __name__ == '__main__':
    manager.run()
