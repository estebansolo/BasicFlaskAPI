from app.models.connection import Manager

class OrdersProducts(Manager):
    def __init__(self):
        self.table = "orders_products"
        self.products_table = "products"

    def products_by_order_id(self, order_id=None):
        if not isinstance(order_id, int):
            return []

        projection = self.select(["op.*", "p.quantity AS inventory", "p.name AS name"])

        select = "SELECT {} FROM {} as op".format(projection, self.table)
        join = "INNER JOIN {} as p ON p.id = op.product_id".format(self.products_table)
        where = "WHERE `order_id` = '{}'".format(order_id)

        return self.execute("{} {} {}".format(select, join, where))
