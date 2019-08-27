from flask import Blueprint, request
from app.api.orders_api import OrdersApi

bp = Blueprint('orders', __name__, url_prefix='/orders')

@bp.route('/<id>', methods=['GET'])
def orders_by_id(id):
	return OrdersApi(request).get_order(id)

@bp.route('/<id>/stock', methods=['GET'])
def order_stock(id):
	return OrdersApi(request).order_products_stock(id)
