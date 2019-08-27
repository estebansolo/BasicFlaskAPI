from app.models.connection import Manager

class ProductsModel(Manager):
    def __init__(self):
        self.table = "products"
        self.orders_products_table = "orders_products"

    def get_inventory(self):
        query = "SELECT id, name, quantity FROM {}".format(self.table)
        return self.execute(query)

    def get_orders_products(self):
        projection = self.select([
            "p.*",
            "op.order_id AS order_id"
        ])

        query = "SELECT {} FROM {} AS p INNER JOIN {} AS op ON p.id = op.product_id".format(
            projection,
            self.table,
            self.orders_products_table
        )

        return self.execute(query)
