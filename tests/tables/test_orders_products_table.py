from mock import patch
from datetime import date
from app.models import OrdersProductsModel

@patch("app.models.connection.Manager.execute")
def test_products_by_order_id_empty_id(mock_execute_query):
    instance = OrdersProductsModel()
    response = instance.products_by_order_id()

    assert response == []
    mock_execute_query.assert_not_called()


@patch("app.models.connection.Manager.execute")
def test_products_by_order_id(mock_execute_query):
    instance = OrdersProductsModel()

    order_id = 1
    response = instance.products_by_order_id(order_id)

    called_query = "SELECT op.*, p.quantity AS inventory, p.name AS name " \
            "FROM orders_products as op INNER JOIN products as p ON p.id = op.product_id " \
            "WHERE `order_id` = '{}'".format(order_id)

    mock_execute_query.assert_called_once_with(called_query)


@patch("app.models.connection.Manager.execute")
def test_sold_products_by_date(mock_execute_query):
    limit = 6
    search_date = "2019-03-01"

    instance = OrdersProductsModel()
    response = instance.sold_products_by_date(search_date=search_date, limit=limit)

    called_query = \
        "SELECT op.product_id AS product_id, p.name AS name, SUM(op.quantity) AS quantity " \
        "FROM orders AS o RIGHT JOIN orders_products AS op ON o.id = op.order_id " \
        "INNER JOIN products AS p ON p.id = op.product_id " \
        "WHERE deliveryDate = '{}' GROUP BY product_id LIMIT {}".format(
            search_date,
            limit
        )

    mock_execute_query.assert_called_once_with(called_query)


@patch("app.models.connection.Manager.execute")
def test_sold_products_by_date_passing_order_by(mock_execute_query):
    limit = 6
    search_date = str(date.today())

    instance = OrdersProductsModel()
    response = instance.sold_products_by_date(limit=limit, order_by=["quantity", "DESC"])

    called_query = \
        "SELECT op.product_id AS product_id, p.name AS name, SUM(op.quantity) AS quantity " \
        "FROM orders AS o RIGHT JOIN orders_products AS op ON o.id = op.order_id " \
        "INNER JOIN products AS p ON p.id = op.product_id " \
        "WHERE deliveryDate = '{}' GROUP BY product_id ORDER BY quantity DESC LIMIT {}".format(
            search_date,
            limit
        )

    mock_execute_query.assert_called_once_with(called_query)
