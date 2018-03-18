from sanic.views import HTTPMethodView
from sanic.response import json
from decorators.signature import signature
from datetime import datetime
import asyncio

# Estou tomando erro aqui!
# from models import Session, Card


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
    await asyncio.sleep(3)
    print("Delayed Task Ran")
