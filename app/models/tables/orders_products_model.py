from datetime import date
from app.models.connection import Manager

class OrdersProductsModel(Manager):
    def __init__(self):
        self.table = "orders_products"
        self.orders_table = "orders"
        self.products_table = "products"

    def products_by_order_id(self, order_id=None):
        if isinstance(order_id, int) or isinstance(order_id, str):
            where_ids = "order_id = '{}'".format(order_id)
        elif isinstance(order_id, list):
            number_to_string = list(map(lambda id: str(id), order_id))
            where_ids = "order_id IN ({})".format(", ".join(number_to_string))
        else:
            return []

        projection = self.select([
            "op.*",
            "p.quantity AS inventory",
            "p.name AS name",
            "p.provider_id AS provider_id",
        ])

        query = "SELECT {} FROM {} as op " \
                "INNER JOIN {} as p ON p.id = op.product_id " \
                "WHERE {}".format(
                    projection,
                    self.table,
                    self.products_table,
                    where_ids
                )

        return self.execute(query)

    def sold_products_by_date(self, search_date="2019-03-01", order_by='asc', limit=None):
        order_by = order_by if order_by.lower() in ["asc", "desc"] else "asc"

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
        query_limit = "LIMIT {}".format(limit) if limit is not None else ""
        ordering_by = "ORDER BY quantity {} ".format(order_by)

        return self.execute(
            "{}{}{}{}{}{}{}".format(
                select,
                right_join,
                inner_join,
                where,
                group_by,
                ordering_by,
                query_limit
            )
        )
