from app.models.connection import Manager

class Orders(Manager):
    def __init__(self):
        self.table = "orders"

    def get_order(self, id=None):
        if not isinstance(id, int):
            return []

        query = "SELECT * FROM {} WHERE `id` = '{}'".format(self.table, id)
        result = self.execute(query)
        return result.pop() if result else {}
