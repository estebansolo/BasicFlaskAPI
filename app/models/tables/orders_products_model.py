from datetime import date
from app.models.connection import Manager

class OrdersProductsModel(Manager):
    def __init__(self):
        self.table = "orders_products"
        self.orders_table = "orders"
        self.products_table = "products"

    def products_by_order_id(self, order_id=None):
        if not isinstance(order_id, int):
            return []

        projection = self.select(["op.*", "p.quantity AS inventory", "p.name AS name"])

        select = "SELECT {} FROM {} as op".format(projection, self.table)
        join = "INNER JOIN {} as p ON p.id = op.product_id".format(self.products_table)
        where = "WHERE `order_id` = '{}'".format(order_id)

        return self.execute("{} {} {}".format(select, join, where))

    def sold_products_by_date(self, search_date="", order_by=None, limit=3):
        ordering_by = ""
        if isinstance(order_by, list) and len(order_by) == 2:
            ordering_by = "ORDER BY {} {} ".format(order_by[0], order_by[1])


        if search_date == "":
            search_date = str(date.today())

        projection = self.select([
            "op.product_id AS product_id",
            "p.name AS name",
            "SUM(op.quantity) AS quantity"
        ])

        select = "SELECT {} FROM {} AS o ".format(projection, self.orders_table)
        right_join = "RIGHT JOIN {} AS op ON o.id = op.order_id ".format(self.table)
        inner_join = "INNER JOIN {} AS p ON p.id = op.product_id ".format(self.products_table)
        where = "WHERE deliveryDate = '{}' ".format(search_date)
        group_by = "GROUP BY product_id "
        limit = "LIMIT {}".format(limit)

        return self.execute(
            "{}{}{}{}{}{}{}".format(
                select,
                right_join,
                inner_join,
                where,
                group_by,
                ordering_by,
                limit
            )
        )
