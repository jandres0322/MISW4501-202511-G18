from app.models.order_model import Order
from app.core.database import db

class OrderRepository:
    @staticmethod
    def get_all():
        return Order.query.all()

    @staticmethod
    def get_by_id(order_id):
        return Order.query.get(order_id)

    @staticmethod
    def create(order_data):
        order = Order(name=order_data["name"], email=order_data["email"])
        db.session.add(order)
        db.session.commit()
        return order