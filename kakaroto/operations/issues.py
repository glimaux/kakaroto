from database.models import Issue
from database.session import Session
from mappers.github import GitHubIssueMapper
from .users import get_or_create_user
# from .labels import create_label


async def create_issue(body, card_id, session=None):
    if session is None:
        session = Session()

    try:
        await get_or_create_user(body['user'], session)

        issue = GitHubIssueMapper(body, card_id)

        issue = Issue().fromdict(issue.__dict__, allow_pk=True)

        session.add(issue)
        session.flush()

        if body['assignees']:
            # TODO: implement async loop
            for assignee in body['assignees']:
                user = await get_or_create_user(assignee, session)
                issue.assignees.append(user)
            session.flush()

        '''
        if body['labels']:
            for label in body['labels':]:
                await create_label(label, body['id'], session)
        '''

    # TODO: add rollback expression
    except Exception as ex:
        print(ex)
