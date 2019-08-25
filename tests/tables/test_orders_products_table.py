from mock import patch
from app.models import OrdersProducts

@patch("app.models.connection.Manager.execute")
def test_products_by_order_id_empty_id(mock_execute_query):
    instance = OrdersProducts()
    response = instance.products_by_order_id()

    assert response == []
    mock_execute_query.assert_not_called()

@patch("app.models.connection.Manager.execute")
def test_products_by_order_id(mock_execute_query):
    instance = OrdersProducts()

    order_id = 1
    response = instance.products_by_order_id(order_id)

    called_query = "SELECT op.*, p.quantity AS inventory, p.name AS name " \
            "FROM orders_products as op INNER JOIN products as p ON p.id = op.product_id " \
            "WHERE `order_id` = '{}'".format(order_id)

    mock_execute_query.assert_called_once_with(called_query)
