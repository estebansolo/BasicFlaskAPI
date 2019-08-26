import json
from mock import patch
from flask import request
from app.controllers.orders_controller import OrdersController

def get_json_content(json_path):
    with open(json_path, 'r') as json_file:
        return json.loads(json_file.read())

def filter_product(product):
    return {
        'quantity': product['quantity'],
        'product_id': product['product_id'],
        'name': product['name']
    }

ORDERS = get_json_content("tests/fixtures/orders.json")
ORDER_PRODUCTS = get_json_content("tests/fixtures/order_products.json")

@patch("app.models.OrdersProductsModel.products_by_order_id", return_value=ORDER_PRODUCTS)
def test_stock_products(mock_order_products_by_id):
    instance = OrdersController(request)

    order_id = 10
    products = list(map(filter_product, ORDER_PRODUCTS))

    response = instance.order_products_stock(order_id)
    result = json.loads(response.data.decode('utf8'))

    assert result == {
        "out_of_stock": [
            {**products[1]}, {**products[2], 'quantity': 2}
        ],
        "in_stock": [
            {**products[0]}, {**products[2], 'quantity': 1}
        ]
    }

    mock_order_products_by_id.assert_called_once_with(order_id)

@patch("app.models.OrdersModel.get_order", return_value=ORDERS[2])
def test_get_order(mock_get_order):
    instance = OrdersController(request)

    order_id = 10
    response = instance.get_order(order_id)
    result = json.loads(response.data.decode('utf8'))

    mock_get_order.assert_called_once_with(order_id)
    assert result == ORDERS[2]


def test_get_stock_information_missing_data():
    response = OrdersController.get_stock_info()
    assert response == {"product_id": 0, "name": "", "quantity": 0}


def test_get_stock_information():
    quantity = 5
    product_info = ORDER_PRODUCTS[1]

    response = OrdersController.get_stock_info(product_info, quantity)
    assert response == {
        "product_id": product_info['product_id'],
        "name": product_info['name'],
        "quantity": quantity
    }
