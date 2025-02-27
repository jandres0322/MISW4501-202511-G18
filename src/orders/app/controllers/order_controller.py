from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService
from app.models.order_model import OrderSchema
from app.utils.response_util import format_response
from app.utils.validate_auth_util import auth_required
from app.exceptions.http_exceptions import NotFoundError, BadRequestError

order_bp = Blueprint('orders', __name__, url_prefix='/orders')
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@order_bp.route('/', methods=['GET'])
@auth_required
def get_orders():
    try:
        orders = OrderService.get_all()
        return format_response("success", 200, message="Todos los pedidos han sido obtenidos", data=orders_schema.dump(orders))
    except ValueError as e:
        return format_response("success", 200, message=str(e), data=[])

@order_bp.route('/<string:id>', methods=['GET'])
def get_order(id:str):
    try:
        order = OrderService.get_by_id(id)
    except (NotFoundError, BadRequestError) as e:
        return format_response("error", e.code, error=e.description)
    else:
        return format_response("success", 200, "Pedido encontrado con éxito", order_schema.dump(order))

    
@order_bp.route('/', methods=['POST'])
def create_order():
    try:
        order_data = request.get_json()
        order = OrderService.create(order_data)
    except BadRequestError as e:
        return format_response("error", e.code, error=e.description)
    else:
        return format_response("success", 201, "Pedido creado con éxito", order_schema.dump(order))
