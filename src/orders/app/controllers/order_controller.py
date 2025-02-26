from flask import Blueprint, request, jsonify
from app.services.order_service import OrderService
from app.models.order_model import OrderSchema
from app.utils.response_util import format_response
from app.exceptions.http_exceptions import NotFoundError, BadRequestError

order_bp = Blueprint('order', __name__, url_prefix='/order')
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

@order_bp.route('/', methods=['GET'])
def get_orders():
    try:
        orders = OrderService.get_all()
        return format_response("success", 200, message="Todos los orderos han sido obtenidos", data=orders_schema.dump(orders))
    except ValueError as e:
        return format_response("success", 200, message=str(e), data=[])

@order_bp.route('/<string:id>', methods=['GET'])
def get_order(id:str):
    try:
        order = OrderService.get_by_id(id)
        return format_response("success", 200, "Ordero encontrado con éxito", order_schema.dump(order))
    except NotFoundError as e:
        return format_response("error", e.code, error=e.description)
    except BadRequestError as e:
        return format_response("error", e.code, error=e.description)