import uuid
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields
from app.core.database import db, ma
from app.utils.product_info_util import get_product_info

class OrderProducts(db.Model):
    __tablename__ = 'order_products'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=db.text("gen_random_uuid()"), unique=True, nullable=False)
    order_id = db.Column(UUID(as_uuid=True), db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(UUID(as_uuid=True), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class OrderProductsSchema(ma.Schema):
    product = fields.Method("get_product")
    class Meta:
        model = OrderProducts
        include_fk = True
        fields = ('id', 'order_id', 'product_id', 'quantity', 'product')

    def get_product(self, obj):
        product = get_product_info(obj.product_id)
        if product:
            return product
        else:
            return {"error": "No se pudo obtener la información del producto"}
