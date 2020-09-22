from flask import Flask
from flask_restful import Api
from resources.tune import Tune, TuneList
import os
from dotenv import load_dotenv

load_dotenv()

RDS_ENDPOINT = os.getenv('RDS_ENDPOINT')
RDS_DB_NAME = os.getenv('RDS_DB_NAME')
RDS_USERNAME = os.getenv('RDS_USERNAME')
RDS_PASSWORD = os.getenv('RDS_PASSWORD')
RDS_PORT = os.getenv('RDS_PORT')
DEV_MODE = True if os.getenv('DEV_MODE') == 'True' else False

URI_STRING = f'mysql+pymysql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_ENDPOINT}:{RDS_PORT}/{RDS_DB_NAME}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = URI_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Tune, '/tune/<int:_id>')
api.add_resource(TuneList, '/tunes')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=DEV_MODE)