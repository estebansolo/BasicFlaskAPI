from flask import Blueprint, request
from app.api.products_api import ProductsApi

bp = Blueprint('products', __name__, url_prefix='/products')

@bp.route('/sold', methods=['GET'])
def sold_products():
    return ProductsApi(request).sold_products()

@bp.route('/inventory', methods=['GET'])
def inventory():
	return ProductsApi(request).new_inventory()

@bp.route('/organize/inventory', methods=['GET'])
def organize_inventory():
	return ProductsApi(request).organize_from_inventory()

@bp.route('/organize/providers', methods=['GET'])
def organize_providers():
	return ProductsApi(request).organize_from_providers()
