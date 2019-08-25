from flask import Response
from app.helpers.utils import serialize_dict_and_list

def flask_request(fun):
    def inner(*args, **kwargs):
        try:
            status = '200'
            result = fun(*args, **kwargs)

        except Exception as error:
            status = '500'
            result = {"error": str(error)}

        return Response(serialize_dict_and_list(result), status)

    return inner
