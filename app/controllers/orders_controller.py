from app.controllers.products_controller import ProductsController
from app.models import OrdersModel, OrdersProductsModel

class OrdersController(object):
    def __init__(self):
        self.orders_model = OrdersModel()
        self.orders_products_model = OrdersProductsModel()


    def get_order_by_id(self, id):
        return self.orders_model.get_order(int(id))


    def get_complete_grouped_orders(self):
        orders = self.get_orders_with_products()
        return OrdersController.get_orders_same_user(orders)


    def get_orders_with_products(self):
        orders = self.get_priorized_orders()
        products = self.get_products_by_orders(orders)
        return self.merge_products_with_orders(orders, products)


    def get_priorized_orders(self):
        orders = self.orders_model.get_all_orders()
        if not orders:
            return orders

        return sorted(orders, key=lambda ord: ord['priority'])


    def get_products_by_orders(self, orders):
        order_ids = list(map(lambda order: order['id'], orders))
        products = self.orders_products_model.products_by_order_id(order_ids)
        return products


    def merge_products_with_orders(self, orders, products):
        for key, order in enumerate(orders):
            filter_products = list(filter(
                lambda product: product['order_id'] == order['id'], products
            ))

            order_products = list(map(ProductsController.clean_product_info, filter_products))
            orders[key]['products'] = order_products

        return orders


    @staticmethod
    def get_orders_same_user(orders, carried_orders=None):
        if carried_orders is None:
            carried_orders = []

        if not orders:
            return carried_orders

        order = orders.pop(0)
        for key, carried in enumerate(carried_orders):
            if carried['address'] == order['address']:
                carried_orders[key]['products'] += order['products']
                break
        else:
            carried_orders.append(order)

        return OrdersController.get_orders_same_user(orders, carried_orders)
