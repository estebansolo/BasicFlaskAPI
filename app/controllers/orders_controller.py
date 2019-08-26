from app.models import OrdersModel, OrdersProductsModel
from app.helpers.decorators import flask_request

class OrdersController(object):
    def __init__(self,request):
        self.orders_model = OrdersModel()
        self.orders_products_model = OrdersProductsModel()


    @flask_request
    def get_order(self, order_id):
        return self.orders_model.get_order(int(order_id))


    @flask_request
    def order_products_stock(self, order_id):
        order_products = self.get_products(order_id)
        in_stock, out_of_stock = OrdersController.get_stock_products(order_products)
        return {"in_stock": in_stock, "out_of_stock": out_of_stock}


    def get_products(self, order_id):
        return self.orders_products_model.products_by_order_id(int(order_id))


    @staticmethod
    def get_stock_products(order_products):
        in_stock, out_of_stock = [], []

        for product in order_products:
            quantity = product.get("quantity", 0)
            inventory = product.get("inventory", 0)
            out_item = quantity - inventory

            if out_item >= 0:
                if inventory > 0:
                    in_stock.append(OrdersController.get_stock_info(product, inventory))

                out_of_stock.append(OrdersController.get_stock_info(product, out_item))
            else:
                quantity = inventory if inventory < quantity else quantity
                in_stock.append(OrdersController.get_stock_info(product, quantity))

        return in_stock, out_of_stock


    @staticmethod
    def get_stock_info(product=None, quantity=0):
        if product is None:
            product = {}

        return {
            "product_id": product.get("product_id", 0),
            "name": product.get("name", ""),
            "quantity": quantity
        }
