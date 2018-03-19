from database.models import Card, GitHubUser
from database.session import Session
from mappers.github import GitHubCardMapper, GitHubUserMapper

# TODO: add issue and place at column
async def create_card(body, session=None):
    if session is None:
        session = Session()

    try:
        get_or_create_user(body['project_card']['creator'], session)

        card = GitHubCardMapper(body)

        item = Card().fromdict(card.__dict__, allow_pk=True)

        session.add(item)
        session.commit()

    except Exception as ex:
        print(ex)

    finally:
        session.close()


def get_or_create_user(body, session=None):
    if session is None:
        session = Session()

    try:
        user = session.query(GitHubUser).get(body['id'])

        if user is None:
            user = GitHubUserMapper(body)

            user = GitHubUser().fromdict(user.__dict__, allow_pk=True)

            session.add(user)
            session.flush()

    except Exception as ex:
        print(ex)
