from app.models.connection import Manager

class ProvidersModel(Manager):
    def __init__(self):
        self.table = "providers"

    def get_providers(self):
        query = "SELECT * FROM {}".format(self.table)
        return self.execute(query)
