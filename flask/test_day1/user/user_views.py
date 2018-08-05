from flask import Blueprint, render_template


blue = Blueprint('first', __name__)


@blue.route('/')
def index():

    return  render_template('hello.html')
