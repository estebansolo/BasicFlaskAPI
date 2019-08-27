from app.controllers.providers_controller import ProvidersController
from app.controllers.products_controller import ProductsController
from app.controllers.orders_controller import OrdersController
from app.helpers.decorators import flask_request

class ProductsApi(object):
    def __init__(self, request):
        self.sort = request.args.get('sort', 'asc')
        self.limit = request.args.get('limit', 3)
        self.search_date = request.args.get('date', '2019-03-01')

        self.orders_controller = OrdersController()
        self.products_controller = ProductsController()
        self.providers_controller = ProvidersController()


    @flask_request
    def sold_products(self):
        return self.products_controller.get_sold_products(
            self.search_date, self.sort, self.limit
        )


    @flask_request
    def new_inventory(self):
        sold_products = self.products_controller.get_sold_products()
        inventory = self.products_controller.get_inventory()

        if not sold_products or not inventory:
            return inventory

        product_list = ProductsController.get_products_list(sold_products)
        return ProductsController.calculate_inventory(inventory, product_list)


    @flask_request
    def organize_from_inventory(self):
        orders, inventory_list = self.calc_products_to_organize()
        return ProductsController.list_products(orders, inventory_list, type="inventory")


    @flask_request
    def organize_from_providers(self):
        orders, inventory_list = self.calc_products_to_organize()
        orders_complete = ProductsController.list_products(orders, inventory_list, type="providers")

        if orders_complete:
            orders_complete = self.providers_controller.set_product_providers(orders_complete)

        return orders_complete


    def calc_products_to_organize(self):
        orders = self.orders_controller.get_complete_grouped_orders()
        inventory = self.products_controller.get_inventory()
        if not orders or not inventory:
            return []

        inventory_list = ProductsController.get_inventory_list(inventory)
        return orders, inventory_list
