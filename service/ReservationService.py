from flask import request, make_response, jsonify

from main import db
from models.reservation import Reservation


def reservation_get():
    reservationservice = Reservation.query.all()
    result = [
        {
            "reservation_no": x.reservation_no,
            "room_num": x.room_num,
            "customers_id": x.customers_id
        } for x in reservationservice]
    return {"count": len(result), "reservationservice": result}


def reservation_post():
    content = request.json
    reservation = Reservation(room_num=content['room_num'],
                              customers_id=content['customers_id']
                              )
    db.session.add(reservation)
    db.session.commit()
    return make_response("", 201)
