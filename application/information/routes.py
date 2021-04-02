from flask import Blueprint, render_template

bp = Blueprint('info', __name__, template_folder="templates")


@bp.route('/')
def home():
    return render_template('index.html')
