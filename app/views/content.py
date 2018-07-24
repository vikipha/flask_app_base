from flask import Blueprint, render_template

from views.decorators import login_required

content_bp = Blueprint('content', __name__)


@content_bp.route("/")
@login_required
def serve_content():
    return render_template("content.html")
