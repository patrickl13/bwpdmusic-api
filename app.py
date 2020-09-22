from flask import Flask
from flask_restful import Api
from resources.tune import Tune, TuneList

URI_STRING = f'mysql+pymysql://{process.env.RDS_USERNAME}:{process.env.RDS_PASSWORD}@{process.env.RDS_ENDPOINT}:{process.env.RDS_PORT}/{process.env.RDS_DB_NAME}'

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