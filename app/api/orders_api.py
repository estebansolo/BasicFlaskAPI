from app.controllers.products_controller import ProductsController
from app.controllers.orders_controller import OrdersController
from app.helpers.decorators import flask_request

class OrdersApi(object):
    def __init__(self, request):
        self.orders_controller = OrdersController()
        self.products_controller = ProductsController()


    @flask_request
    def get_order(self, order_id):
        return self.orders_controller.get_order_by_id(order_id)


    @flask_request
    def order_products_stock(self, order_id):
        order_products = self.products_controller.get_products(order_id)
        in_stock, out_of_stock = ProductsController.get_stock_products(order_products)
        return {"in_stock": in_stock, "out_of_stock": out_of_stock}
