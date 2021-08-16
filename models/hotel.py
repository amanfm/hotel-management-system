from sqlalchemy.orm import relationship
from main import db
from models.room import Room


class Hotel(db.Model):
    __tablename__ = 'hotel'
    hotel_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(20), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    room_num = db.Column(db.Integer, db.ForeignKey('room.room_no'))

    room = relationship(Room)

    def __init__(self, city, state, phone, room_num):
        # self.hotel_id = hotel_id
        self.city = city
        self.state = state
        self.phone = phone
        self.room_num = room_num

    def __repr__(self):
        return '<User %r>' % self.city


# db.create_all()
