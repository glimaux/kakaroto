from database.models import GitHubUser
from database.session import Session
from mappers.github import GitHubUserMapper


async def get_or_create_user(body, session=None):
    if session is None:
        session = Session()

    try:
        user = session.query(GitHubUser).get(body['id'])

        if user is None:
            user = GitHubUserMapper(body)

            user = GitHubUser().fromdict(user.__dict__, allow_pk=True)

            session.add(user)
            session.flush()

        return user
    # TODO: add rollback expression
    except Exception as ex:
        print(ex)
