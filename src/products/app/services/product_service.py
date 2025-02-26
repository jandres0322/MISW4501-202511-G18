import uuid
from app.repositories.product_repository import ProductRepository
from app.exceptions.http_exceptions import BadRequestError, NotFoundError

def validate_uuid(id):
    try:
        uuid.UUID(id, version=4)
        return True
    except ValueError:
        return False

class ProductService:
    @staticmethod
    def get_all():
        products = ProductRepository.get_all()
        if not products:
            raise ValueError("No hay productos registrados")
        return products

    @staticmethod
    def get_by_id(product_id):

        if not validate_uuid(product_id):
            raise BadRequestError("El formato del id del producto no es correcto")
        
        product = ProductRepository.get_by_id(product_id)
        if not product:
            raise NotFoundError("Producto no encontrado")
        return product

    @staticmethod
    def create(product_data):
        return ProductRepository.create(product_data)