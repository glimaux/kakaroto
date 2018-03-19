from database.models import Card
from database.session import Session
from mappers.github import GitHubCardMapper
from .users import get_or_create_user
from .issues import create_issue
from .card_moves import create_card_move
from agents.github import get_issue


async def create_card(body, session=None):
    if session is None:
        session = Session()

    # TODO: add issue and place at column
    try:
        await get_or_create_user(body['project_card']['creator'], session)

        card = GitHubCardMapper(body['project_card'])

        card = Card().fromdict(card.__dict__, allow_pk=True)

        session.add(card)
        session.flush()

        await create_card_move(body['project_card'], session)

        if "content_url" in body['project_card']:
            issue = await get_issue(body['project_card']["content_url"])
            await create_issue(issue, body['project_card']['id'], session)

        session.commit()

    # TODO: add rollback expression
    except Exception as ex:
        print(ex)

    finally:
        session.close()
