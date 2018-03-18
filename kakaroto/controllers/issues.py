from sanic.views import HTTPMethodView
from sanic.response import json
from decorators.signature import signature


class Webhook(HTTPMethodView):
    decorators = [signature]
    pass
