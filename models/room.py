from main import db


class Room(db.Model):
    room_no = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.String(20), nullable=False)
    rates = db.Column(db.Integer, nullable=False)


def __init__(self, room_type, rates):
    # self.room_no = room_no
    self.room_type = room_type
    self.rates = rates


db.create_all()
