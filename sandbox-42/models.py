from api_data_app import db


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer)
    response = db.Column(db.Text)
    datetime = db.Column(db.DateTime)

    def __init__(self, uuid, response, datetime):
        self.uuid = uuid
        self.response = response
        self.datetime = datetime

    def __repr__(self):
        return '<Data %r>' % self.response


class Logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer)
    payload = db.Column(db.Text)
    datetime = db.Column(db.DateTime)

    def __init__(self, uuid, payload, datetime):
        self.uuid = uuid
        self.payload = payload
        self.datetime = datetime

    def __repr__(self):
        return '<Data %r>' % self.payload
