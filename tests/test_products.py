import pytest
from mock import patch
from app.app import create_app

@pytest.fixture
def client():
    api = create_app()
    return api.test_client(use_cookies=False)


def decode_api_response(res):
    return res.data.decode('utf8')


def test_most_sold_not_allowed(client):
    url = '/products/sold/most'
    response = client.post(url)
    assert response.status == '405 METHOD NOT ALLOWED'

    response = client.put(url)
    assert response.status == '405 METHOD NOT ALLOWED'


@patch("app.controllers.products_controller.ProductsController.most_sold")
def test_most_sold(mock_most_sold, client):
    client.get('/products/sold/most')
    mock_most_sold.assert_called()


def test_fewer_sold_not_allowed(client):
    url = '/products/sold/fewer'
    response = client.post(url)
    assert response.status == '405 METHOD NOT ALLOWED'

    response = client.put(url)
    assert response.status == '405 METHOD NOT ALLOWED'


@patch("app.controllers.products_controller.ProductsController.fewer_sold")
def test_order_stock(mock_fewer_sold, client):
    client.get('/products/sold/fewer')
    mock_fewer_sold.assert_called()
