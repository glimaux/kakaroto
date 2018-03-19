from database.models import CardMoveHistory
from database.session import Session
from mappers.github import GitHubCardMoveMapper


async def create_card_move(body, session=None):
    if session is None:
        session = Session()

    try:
        move = GitHubCardMoveMapper(body)

        move = CardMoveHistory().fromdict(move.__dict__)

        session.add(move)
        session.flush()

    # TODO: add rollback expression
    except Exception as ex:
        print(ex)
