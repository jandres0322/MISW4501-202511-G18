from app.models.product_model import Product
from app.core.database import db

class ProductRepository:
    @staticmethod
    def get_all():
        return Product.query.all()

    @staticmethod
    def get_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def create(product_data):
        product = Product(name=product_data["name"], email=product_data["email"])
        db.session.add(product)
        db.session.commit()
        return product