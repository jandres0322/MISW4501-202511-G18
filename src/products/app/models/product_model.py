import uuid
from app.core.database import db, ma
from sqlalchemy.dialects.postgresql import UUID

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=db.text("gen_random_uuid()"), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cetegory = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def __repr__(self):
        return '<Product %r>' % self.username
    
class ProductSchema(ma.Schema):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'category', 'price', 'amount', 'created_at', 'updated_at')
    