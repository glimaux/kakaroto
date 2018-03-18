from functools import wraps
from sanic.response import json
import hmac
from hashlib import sha1

from config import GITHUB


def signature(func):
    @wraps(func)
    async def signature_wrapper(request, *args, **kwargs):
        is_authorized = check_signature(request)

        if is_authorized:
            response = await func(request, *args, **kwargs)
            return response
        else:
            # TODO: Alterar o código de erro e a mensagem para um referência a um Enum de erros
            return json(
                {
                    'success': 'false',
                    'errors': [
                        {
                            'code': 401000,
                            'message': "You are not allowed to access this operation"

                        }
                    ]
                },
                401
            )
    return signature_wrapper


def check_signature(request):

    try:
        git_signature = request.headers['X-Hub-Signature']
        signature_bytes = hmac.new(
            GITHUB['WEBHOOK_SIGNATURE_KEY'].encode(),
            msg=request.body,
            digestmod=sha1
        )
        signature = 'sha1=' + signature_bytes.hexdigest()

        is_safe = hmac.compare_digest(git_signature, signature)

        return is_safe

    except KeyError:
        return False
