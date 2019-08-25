import json
from app.helpers.datetime import dates_serializer

def serialize_dict_and_list(data):
    if isinstance(data, dict) or isinstance(data, list):
        data = json.dumps(data, default=dates_serializer)

    return data
