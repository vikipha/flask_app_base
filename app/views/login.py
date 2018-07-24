import flask
from flask import render_template, Blueprint, request, redirect, make_response

from models.user import User

login_bp = Blueprint('login', __name__)


@login_bp.route("/", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        login_ = request.form.get('login')
        password = request.form.get('password')
        user = User.find_by_credentials(login_, password)

        if user:
            flask.session['user_id'] = user.id
            return make_response(redirect('/content'))
        else:
            flask.session.clear()

    return render_template("login.html")


@login_bp.route("/logout/")
def logout():
    flask.session.clear()
    return render_template('logout.html')
