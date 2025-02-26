import uuid
from app.core.database import db, ma
from sqlalchemy.dialects.postgresql import UUID

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=db.text("gen_random_uuid()"), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    
    def __repr__(self):
        return '<Order %r>' % self.username
    
class OrderSchema(ma.Schema):
    class Meta:
        model = Order
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')
    