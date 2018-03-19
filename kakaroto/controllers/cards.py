from sanic.views import HTTPMethodView
from sanic.response import json
from decorators.signature import signature
from resolvers.card_webhook_action_resolver import card_webhook_action_resolver


class Webhook(HTTPMethodView):
    decorators = [signature]

    async def post(self, request):
        request.app.add_task(process_request(request))
        return json(
            {
                "success": "true"
            }
        )


async def process_request(request):
    try:
        if request.json['action'] in card_webhook_action_resolver:
            operation = card_webhook_action_resolver[request.json['action']]

            await operation(request.json)
    except Exception as ex:
        print(ex.args)
