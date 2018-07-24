from functools import wraps
from typing import Callable

import flask
from flask import redirect


def login_required(f):
    # type: (Callable) -> Callable

    @wraps(f)
    def inner(*args, **kwargs):
        if flask.session.get("user_id"):
            return f(*args, **kwargs)
        else:
            return redirect("/login/")

    return inner
