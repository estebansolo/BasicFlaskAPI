from app.models import ProvidersModel

class ProvidersController(object):
    def __init__(self):
        self.providers_model = ProvidersModel()

    def set_product_providers(self, orders):
        providers = self.get_providers()
        for key, order in enumerate(orders):
            if 'products' in order and order['products']:
                for product_key, product in enumerate(order['products']):
                    if product['provider_id'] in providers:
                        orders[key]['products'][product_key]['provider'] = {
                            "id": product['provider_id'],
                            "name": providers[product['provider_id']]
                        }

        return orders


    def get_providers(self):
        providers = self.providers_model.get_providers()
        return {provider['id']: provider['name'] for provider in providers}
