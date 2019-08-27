from app.models import OrdersProductsModel, ProductsModel, OrdersModel

class ProductsController(object):
    def __init__(self):
        self.products_model = ProductsModel()
        self.orders_products_model = OrdersProductsModel()


    def get_products(self, id):
        return self.orders_products_model.products_by_order_id(int(id))


    def get_sold_products(self, search_date='2019-03-01', order_by='asc', limit=None):
        params = {
            "limit": limit,
            "order_by": order_by,
            "search_date": search_date
        }

        return self.orders_products_model.sold_products_by_date(**params)


    def get_inventory(self):
        return self.products_model.get_inventory()


    @staticmethod
    def get_stock_products(order_products):
        in_stock, out_of_stock = [], []

        for product in order_products:
            quantity = product.get("quantity", 0)
            inventory = product.get("inventory", 0)
            out_item = quantity - inventory

            if out_item >= 0:
                if inventory > 0:
                    in_stock.append(ProductsController.get_stock_info(product, inventory))

                out_of_stock.append(ProductsController.get_stock_info(product, out_item))
            else:
                quantity = inventory if inventory < quantity else quantity
                in_stock.append(ProductsController.get_stock_info(product, quantity))

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


    @staticmethod
    def get_products_list(sold_products):
        return {
            product.get('product_id', 0): product.get('quantity', 0)
            for product in sold_products
        }


    @staticmethod
    def calculate_inventory(inventory, product_list):
        new_inventory = []
        for product in inventory:
            if product['id'] in product_list:
                quantity = product['quantity'] - product_list[product['id']]
                product['quantity'] = quantity if quantity >= 0 else 0

            new_inventory.append(product)

        return new_inventory


    @staticmethod
    def clean_product_info(product):
        return {
            "id": product['product_id'],
            "name": product['name'],
            "quantity": product['quantity'],
            "provider_id": product.get('provider_id')
        }


    @staticmethod
    def get_inventory_list(inventory):
        return {
            product.get('id', 0): product.get('quantity', 0)
            for product in inventory
        }


    @staticmethod
    def list_products(orders, inventory_list, type=""):
        filter_order = []
        for key, order in enumerate(orders):
            order_products = []
            for product_key, product in enumerate(order['products']):
                add, quantity, new_inventory = ProductsController.calc_inventory_on_products(
                    product, inventory_list, type
                )

                if add:
                    product['quantity'] = product['quantity'] if quantity is None else quantity
                    order_products.append(product)

                inventory_list = new_inventory

            if order_products:
                filter_order.append({**order, "products": order_products})

        return filter_order

    @staticmethod
    def calc_inventory_on_products(product, inventory_list, type):
        quantity = None
        add_product = False
        if product['id'] not in inventory_list or not inventory_list[product['id']]:
            add_product = True if type == "providers" else False
        elif inventory_list[product['id']] >= product['quantity']:
            inventory_list[product['id']] -= product['quantity']
            if inventory_list[product['id']] == 0:
                del inventory_list[product['id']]

            if type == "inventory":
                add_product = True
        else:
            add_product = True
            quantity = inventory_list[product['id']] if type == "inventory" else product['quantity'] - inventory_list[product['id']]
            del inventory_list[product['id']]

        return add_product, quantity, inventory_list
