from app.models import OrdersProductsModel
from app.helpers.decorators import flask_request

class ProductsController(object):
    def __init__(self, request):
        self.limit = request.args.get('limit', 3)
        self.search_date = request.args.get('date', '')
        self.orders_products_model = OrdersProductsModel()


    @flask_request
    def most_sold(self):
        order = ["quantity", "DESC"]
        return self.get_sold_products(order_by=order)


    @flask_request
    def fewer_sold(self):
        order = ["quantity", "ASC"]
        return self.get_sold_products(order_by=order)


    def get_sold_products(self, order_by=None):
        params = {
            "limit": self.limit,
            "order_by": order_by,
            "search_date": self.search_date
        }

        return self.orders_products_model.sold_products_by_date(**params)
