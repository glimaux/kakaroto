from sanic.views import HTTPMethodView
from sanic.response import json

from decorators.authorization import authorization
from database.models import Project
from database.session import Session
from extensions.json import extended_dumps


class Collection(HTTPMethodView):
    decorators = [authorization]

    # TODO: Adicionar validação como decorator
    async def post(self, request):
        session = Session()
        try:
            item = Project().fromdict(request.json, allow_pk=True)

            session.add(item)
            session.commit()

            # TODO: controle dos contratos das repostas de forma centralizada -> return SuccessReponse(item.asdict)
            return json(
                {
                    'success': True,
                    'data': item.asdict()
                },
                status=201,
                dumps=extended_dumps
            )

        finally:
            session.close()
