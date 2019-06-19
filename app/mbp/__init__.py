from flask import Blueprint

bp = Blueprint('mbp', __name__)

from app.mbp import routes
