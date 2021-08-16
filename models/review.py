from sqlalchemy.orm import relationship

from main import db
from models.customer import Customer
from models.hotel import Hotel


class Review(db.Model):
    __tablename__ = 'review'
    review_no = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.Integer, nullable=False)
    customers_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'))
    hotel_ids = db.Column(db.Integer, db.ForeignKey('hotel.hotel_id'))

    customer = relationship(Customer)
    hotel = relationship(Hotel)

    def __init__(self, review, customers_id, hotel_ids):
        # self.review_no = review_no
        self.review = review
        self.customers_id = customers_id
        self.hotel_ids = hotel_ids


db.create_all()
