import pytest
from app.app import create_app

@pytest.fixture
def client():
    api = create_app()
    return api.test_client(use_cookies=False)

def decode_api_response(res):
    return res.data.decode('utf8')

def test_order_bad_methods(client):
    response = client.post('/pedidos/4/productos')
    assert response.status == '405 METHOD NOT ALLOWED'

    response = client.put('/pedidos/4/productos')
    assert response.status == '405 METHOD NOT ALLOWED'

def test_order_endpoint(client):
    ID_PEDIDO = 4
    response = client.get('/pedidos/{}/productos'.format(ID_PEDIDO))
    body_response = decode_api_response(response)
    assert int(body_response) == ID_PEDIDO
    assert response.status == "200"
