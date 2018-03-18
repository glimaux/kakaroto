from sanic.views import HTTPMethodView
from sanic.response import json
from decorators.authorization import authorization

from database.models import Project
from database.session import Session


class Collection(HTTPMethodView):
    decorators = [authorization]

    # TODO: Adicionar validação como decorator
    async def post(self, request):
        session = Session()
        try:
            item = Project().fromdict(request.json, allow_pk=True)

            session.add(item)
            session.commit()

            # TODO: Ajustar serialização de datetime (atualmente está transformando em timestamp)
            return json(
                {
                    'success': True,
                    'data': item.asdict()
                },
            )

        finally:
            session.close()
