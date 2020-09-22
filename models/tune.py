from db import db


class TuneModel(db.Model):
    __tablename__ = 'tunes'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    time_signature = db.Column(db.String(80))
    style = db.Column(db.String(80))
    composer = db.Column(db.String(80))
    file_url = db.Column(db.String(80))

    def __init__(_id, self, name, time_signature, style, composer, file_url):
        self.id = _id
        self.name = name
        self.time_signature = time_signature
        self.style = style
        self.composer = composer
        self.file_url = file_url

    def json(self):
        return {
            'id': self.id,
            'name': self.name, 
            'time_signature': self.time_signature,
            'style': self.style,
            'composer': self.composer,
            'file_url': self.file_url
            }

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()