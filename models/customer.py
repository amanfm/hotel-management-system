from main import db


class Customer(db.Model):
    __tablename__ = 'customer'
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)

    def __init__(self, first_name, last_name):
        # self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

