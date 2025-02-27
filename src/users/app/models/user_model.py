import uuid
import enum
from app.core.database import db, ma
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow_enum import EnumField

class StatusEnum(enum.Enum):
    BLOCKED = "blocked"
    ACTIVE = "active"
    INACTIVE = "inactive"

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(StatusEnum), nullable=False, default=StatusEnum.ACTIVE)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.username = email.split('@')[0]
        self.password = generate_password_hash(password)
        super().__init__()
    
    def __repr__(self):
        return '<User %r>' % self.username
    
    def check_password(self, password):
        return check_password_hash(self.password, str(password))
    
class UserSchema(ma.Schema):
    status = EnumField(StatusEnum, by_value=True)
    class Meta:
        model = User
        fields = ('id', 'name', 'lastname', 'username', 'email', 'status', 'created_at', 'updated_at')
    