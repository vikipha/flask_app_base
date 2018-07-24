from typing import Any

from flask import Flask

import config
from core.database import db_session
from views.content import content_bp
from views.login import login_bp
from core.logging import setup_logging


setup_logging()
app = Flask(__name__, template_folder='templates')
app.secret_key = config.SECRET_KEY
app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(content_bp, url_prefix="/content")


@app.teardown_appcontext
def shutdown_session(exception: Any = None) -> None:
    db_session.remove()


if __name__ == "__main__":
    # Just to simplify debugging
    app.run("0.0.0.0", 5000, debug=True)
