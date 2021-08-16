from flask import request, make_response, jsonify

from main import db
from models.room import Room


def room_get():
    roomservice = Room.query.all()
    result = [
        {
            "room_no": x.room_no,
            "room_type": x.room_type,
            "rates": x.rates
        } for x in roomservice]
    return {"count": len(result), "roomservice": result}


def room_post():
    content = request.get_json()
    new_room = Room(room_type=content['room_type'],
                    rates=content['rates'])
    db.session.add(new_room)
    db.session.commit()
    return make_response("", 201)
