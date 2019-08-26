import json
from decimal import *
from datetime import datetime, date

def serialize_dict_and_list(data):
    if isinstance(data, dict) or isinstance(data, list):
        data = json.dumps(data, default=json_serializer)

    return data

def json_serializer(elem):
    if isinstance(elem, date) or isinstance(elem, datetime):
        return elem.__str__()
    elif(isinstance(elem, Decimal)):
        return int(elem)
