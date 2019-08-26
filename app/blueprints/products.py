from flask import Blueprint, current_app, request
from app.controllers.products_controller import ProductsController

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/sold/most', methods=['GET'])
def most_sold():
    return ProductsController(request).most_sold()

@bp.route('/sold/fewer', methods=['GET'])
def fewer_sold():
	return ProductsController(request).fewer_sold()
