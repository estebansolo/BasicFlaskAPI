from datetime import datetime, date

def dates_serializer(elem):
    if isinstance(elem, date) or isinstance(elem, datetime):
        return elem.__str__()
