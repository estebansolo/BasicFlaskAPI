from flask import Blueprint, current_app, request
from app.controllers.orders_controller import OrdersController

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('/<id>', methods=['GET'])
def orders_by_id(id):
	return OrdersController(request).get_order(id)

@bp.route('/<id>/stock', methods=['GET'])
def order_stock(id):
	return OrdersController(request).order_products_stock(id)
