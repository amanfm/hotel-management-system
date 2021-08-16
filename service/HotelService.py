from flask import request, make_response, jsonify

from main import db
from models.hotel import Hotel


def hotel_get():
    hotelservice = Hotel.query.all()
    result = [
        {
            "hotel_id": x.hotel_id,
            "city": x.city,
            "state": x.state,
            "phone": x.phone,
            "room_num": x.room_num
        } for x in hotelservice]
    return {"count": len(result), "hotelservice": result}


def hotel_post():
    content = request.json
    hotel = Hotel(city=content['city'],
                  state=content['state'],
                  phone=content['phone'],
                  room_num=content['room_num']
                  )
    db.session.add(hotel)
    db.session.commit()
    return make_response("", 201)
