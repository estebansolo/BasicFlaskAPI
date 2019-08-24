import json

class OrdersController(object):
    def __init__(self, request, response):
        self.request = request
        self.response = response

    def products_by_order(self, id):
        self.response.data = id
        self.response.status = '200'
        return self.response
