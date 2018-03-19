from json import dumps, loads
import datetime
import decimal
from uuid import UUID


def extended_encoder(obj):
    if isinstance(obj, (datetime.date, datetime.datetime)):
        return obj.isoformat()

    if isinstance(obj, decimal.Decimal):
        return float(obj)

    if isinstance(obj, UUID):
        return str(obj)


def extended_dumps(obj, extensions=extended_encoder, **kwargs):
    return dumps(obj, default=extensions)


def extended_loads(raw, **kwarfs):
    return loads(raw)
