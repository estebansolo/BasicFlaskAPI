from app.controllers.orders import OrdersController
from flask import Blueprint, request, Response, current_app

bp = Blueprint('orders', __name__, url_prefix='/pedidos')

orders = OrdersController(request, Response())

@bp.route('/<id>/productos', methods=['GET'])
def orders_by_id(id):
	return orders.products_by_order(id)
