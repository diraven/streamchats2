import json
from django.http import HttpResponse

__author__ = 'diraven'

class HttpResponseJson(HttpResponse):
    def __init__(self, data=None, is_success=False, message=''):
        response_data = {
            'data': data,
            'message': message,
            'success': is_success
        }
        super(HttpResponseJson, self).__init__(json.dumps(response_data), content_type="application/json")