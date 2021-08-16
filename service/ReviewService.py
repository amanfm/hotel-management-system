from flask import request, make_response, jsonify

from main import db
from models.review import Review


def review_get():
    reviewservice = Review.query.all()
    result = [
        {
            "review_no": x.review_no,
            "review": x.review,
            "customers_id": x.customers_id,
            "hotel_ids": x.hotel_ids
        } for x in reviewservice]
    return {"count": len(result), "reviewservice": result}


def review_post():
    content = request.json
    review = Review(review=content['review'],
                    customers_id=content['customers_id'],
                    hotel_ids=content['hotel_ids']
                    )
    db.session.add(review)
    db.session.commit()
    return make_response("", 201)
