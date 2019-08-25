from flask import Blueprint, request, current_app
from app.controllers.orders_controller import OrdersController

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('/<id>', methods=['GET'])
def orders_by_id(id):
	orders = OrdersController(request)
	return orders.get_order(id)

@bp.route('/<id>/stock', methods=['GET'])
def order_stock(id):
	orders = OrdersController(request)
	return orders.order_products_stock(id)
