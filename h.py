from flask import Flask, url_for
from flask import request


app = Flask(__name__)


def do_the_login():
    print('done login')
    return 'done post'

def show_the_login_form():
    print('form')
    return 'done get'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

