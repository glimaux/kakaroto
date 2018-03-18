from functools import wraps
from sanic.response import json
import hmac
from hashlib import sha1

from config import GITHUB


def authorization(func):
    @wraps(func)
    async def authorization_wrapper(request, *args, **kwargs):
        is_authorized = validate_authorization(request)

        if is_authorized:
            response = await func(request, *args, **kwargs)
            return response
        else:
            # TODO: Alterar o código de erro e a mensagem para um referência a um Enum de erros
            return json(
                {
                    'success': False,
                    'errors': [
                        {
                            'code': 401000,
                            'message': "You are not allowed to access this operation"

                        }
                    ]
                },
                401
            )
    return authorization_wrapper


def validate_authorization(request):

    try:
        authorization = request.token

        # TODO: Enviar request para um validador de identidade externo
        # ou dar suporte a gestão de clientes dentro da API

        return True

    except KeyError:
        return False
