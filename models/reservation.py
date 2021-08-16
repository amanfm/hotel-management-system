from sqlalchemy.orm import relationship

from main import db
from models.customer import Customer
from models.room import Room


class Reservation(db.Model):
    __tablename__ = 'reservation'
    reservation_no = db.Column(db.Integer, primary_key=True)
    room_num = db.Column(db.Integer, db.ForeignKey('room.room_no'))
    customers_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))

    room = relationship(Room)
    customer = relationship(Customer)

    def __init__(self, room_num, customers_id):
        # self.reservation_no = reservation_no
        self.room_num = room_num
        self.customers_id = customers_id

db.create_all()