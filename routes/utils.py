import sys

sys.path.append("..")

from response.error import HTTPError
from response.response import Response


def modify_response(func):
    
    def inner(*args, **kwargs):
        try:
            body = func(*args, **kwargs)
            body = body.encode('utf-8')
            contentType = 'application/json; charset=utf-8'
            headers = [('Content-Type', contentType),
                                 ('Content-Length', len(body))]
            return Response(200, 'OK', headers, body)
        except Exception as e:
            raise HTTPError(404, str(e))

    return inner
