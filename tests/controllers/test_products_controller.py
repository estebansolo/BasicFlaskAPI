import json
from mock import patch
from flask import request
from app.controllers.products_controller import ProductsController

def get_json_content(json_path):
    with open(json_path, 'r') as json_file:
        return json.loads(json_file.read())

SOLD_PRODUCTS = get_json_content("tests/fixtures/sold_products.json")

def filter_sold_products(reverse=False):
    sold_filtered = sorted(SOLD_PRODUCTS, key=lambda prod: prod['quantity'], reverse=reverse)
    return sold_filtered[:3]

@patch("flask.request")
@patch("app.models.OrdersProductsModel.sold_products_by_date")
def test_fewer_sold(mock_sold_products_by_date, mock_request):
    mock_request.args.return_value = {}
    mock_sold_products_by_date.return_value = filter_sold_products()

    response = ProductsController(mock_request).fewer_sold()
    result = json.loads(response.data.decode('utf8'))
    assert result == [SOLD_PRODUCTS[5], SOLD_PRODUCTS[1], SOLD_PRODUCTS[2]]

@patch("flask.request")
@patch("app.models.OrdersProductsModel.sold_products_by_date")
def test_most_sold(mock_sold_products_by_date, mock_request):
    mock_request.args.return_value = {}
    mock_sold_products_by_date.return_value = filter_sold_products(True)

    response = ProductsController(mock_request).most_sold()
    result = json.loads(response.data.decode('utf8'))
    assert result == [SOLD_PRODUCTS[0], SOLD_PRODUCTS[4], SOLD_PRODUCTS[7]]
