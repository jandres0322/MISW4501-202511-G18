from flask import Blueprint
from app.services.product_service import ProductService
from app.models.product_model import ProductSchema
from app.utils.response_util import format_response
from app.utils.validate_auth_util import auth_required
from app.exceptions.http_exceptions import NotFoundError, BadRequestError

product_bp = Blueprint('products', __name__, url_prefix='/products')
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@product_bp.route('/', methods=['GET'])
@auth_required
def get_products():
    try:
        products = ProductService.get_all()
        return format_response("success", 200, message="Todos los productos han sido obtenidos", data=products_schema.dump(products))
    except ValueError as e:
        return format_response("success", 200, message=str(e), data=[])

@product_bp.route('/<string:id>', methods=['GET'])
@auth_required
def get_product(id:str):
    try:
        product = ProductService.get_by_id(id)
        return format_response("success", 200, "Producto encontrado con éxito", product_schema.dump(product))
    except (NotFoundError, BadRequestError) as e:
        return format_response("error", e.code, error=e.description)
    
@product_bp.route('/ping', methods=['GET'])
def ping():
    return format_response("success", 200, "pong")