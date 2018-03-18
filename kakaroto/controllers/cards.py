from sanic.views import HTTPMethodView
from sanic.response import json
from decorators.signature import signature
from datetime import datetime
import asyncio

# Estou tomando erro aqui!
from models import Session, Card


class Webhook(HTTPMethodView):
    decorators = [signature]

    async def post(self, request):
        # Como posso fazer para chamar uma task em background aqui? Preciso utilizar o app
        # app.add_task(process_request(request))
        return json(
            {
                "success": "true"
            }
        )


async def process_request(request):
    await asyncio.sleep(0.5)
    print("Delayed Task Ran")
