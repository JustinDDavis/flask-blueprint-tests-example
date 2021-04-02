from flask import Blueprint, render_template

bp = Blueprint('blog', __name__, template_folder="templates")


@bp.route('/blog')
def index():
    return render_template('index.html')
