
from flask import Blueprint, render_template

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/')
def index():
    return render_template('index.html')