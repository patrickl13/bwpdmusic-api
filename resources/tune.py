from flask_restful import Resource, reqparse
from models.tune import TuneModel


class Tune(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        required=True,
                        help="name is required"
                        )
    parser.add_argument('time_signature',
                        required=True,
                        help="time signature is required"
                        )
    parser.add_argument('style',
                        required=True,
                        help="style is required"
                        )
    parser.add_argument('composer',
                        required=True,
                        help="composer is required"
                        )
    parser.add_argument('file_url',
                        required=True,
                        help="File url is required"
                        )
    
    def get(self, _id):
        tune = TuneModel.find_by_id(_id)
        if tune:
            return tune.json()
        return {'message': 'Tune not found'}, 404

    def post(self, _id):
        data = Tune.parser.parse_args()
        tune = TuneModel(**data)

        try:
            tune.save_to_db()
        except:
            return {"message": "An error occurred inserting the tune."}, 500

        return tune.json(), 201

    def delete(self, _id):
        tune = TuneModel.find_by_id(_id)
        if tune:
            tune.delete_from_db()
            return {'message': 'Tune deleted.'}
        return {'message': 'Tune not found.'}, 404

    def put(self, _id):
        data = Tune.parser.parse_args()

        tune = TuneModel.find_by_id(_id)

        if tune:
            tune.name = data['name']
            tune.time_signature = data['time_signature']
            tune.style = data['style']
            tune.composer = data['composer']
            tune.file_url = data['file_url']
        else:
            tune = TuneModel(_id, **data)

        tune.save_to_db()

        return tune.json()


class TuneList(Resource):
    def get(self):
        return {'tunes': list(map(lambda x: x.json(), TuneModel.query.all()))}
