from flask import Blueprint, jsonify

from models.data import Data, data_schema_many

base = Blueprint('base', __name__)


@base.route('/')
def index():
    data = Data.query.all()
    return data_schema_many.jsonify(data)