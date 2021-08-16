from flask import request, make_response, jsonify

from main import db
from models.customer import Customer


def customer_get():
    customerservice = Customer.query.all()
    result = [
        {
            "customer_id ": x.customer_id ,
            "first_name": x.first_name,
            "last_name": x.last_name
        } for x in customerservice]
    return {"count": len(result), "customerservice ": result}


def customer_post():
    content = request.json
    customer = Customer(first_name=content['first_name'],
                        last_name=content['last_name']
                        )
    db.session.add(customer)
    db.session.commit()
    return make_response("", 201)
