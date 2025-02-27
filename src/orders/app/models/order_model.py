import uuid
from sqlalchemy.dialects.postgresql import UUID
from app.core.database import db, ma
from app.models.order_product_model import OrderProducts

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=db.text("gen_random_uuid()"), unique=True, nullable=False)
    id_user = db.Column(UUID(as_uuid=True), unique=True, nullable=False)
    #total = db.Column(db.Integer, nullable=False)
    #product_quantity = db.Column(db.Text, nullable=False)
    delivery_date = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    order_products = db.relationship("OrderProducts", backref="order", cascade="all, delete-orphan")
    
    def __repr__(self):
        return '<Order %r>' % self.username
    
class OrderSchema(ma.Schema):
    class Meta:
        model = Order
        fields = ('id', 'id_user', 'delivery_date', 'created_at', 'updated_at', 'order_products')
    