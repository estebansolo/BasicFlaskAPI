from app.models.connection import Manager

class OrdersModel(Manager):
    def __init__(self):
        self.table = "orders"
        self.products_table = "products"
        self.orders_products_table = "orders_products"

    def get_order(self, id=None):
        if not isinstance(id, int):
            return {}

        query = "SELECT * FROM {} WHERE `id` = '{}'".format(self.table, id)
        result = self.execute(query)
        return result.pop() if result else {}

    def get_all_orders(self):
        query = "SELECT * FROM {}".format(self.table)
        return self.execute(query)
