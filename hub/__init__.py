from flask import Blueprint, Flask, render_template

app = Flask(__name__)
blu = Blueprint('big', __name__)