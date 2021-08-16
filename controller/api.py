from main import app
from service.CustomerService import customer_get, customer_post
from service.HotelService import hotel_get, hotel_post
from service.ReservationService import reservation_get, reservation_post
from service.ReviewService import review_get, review_post
from service.RoomService import room_post, room_get

app.add_url_rule("/api/hotel-view", "hotel-view", hotel_get, methods=['GET'])
app.add_url_rule("/api/hotel-data", "hotel-data", hotel_post, methods=['POST'])

app.add_url_rule("/api/room-view", "room-view", room_get, methods=['GET'])
app.add_url_rule("/api/room-post", "room-post", room_post, methods=['POST'])

app.add_url_rule("/api/reservation-view", "reservation-view", reservation_get, methods=['GET'])
app.add_url_rule("/api/reservation-post", "reservation-post", reservation_post, methods=['POST'])

app.add_url_rule("/api/customer-view", "customer-view", customer_get, methods=['GET'])
app.add_url_rule("/api/customer-post", "customer-post", customer_post, methods=['POST'])

app.add_url_rule("/api/review-view", "review-view", review_get, methods=['GET'])
app.add_url_rule("/api/review-post", "review-post", review_post, methods=['POST'])

if __name__ == '__main__':
    app.run()
