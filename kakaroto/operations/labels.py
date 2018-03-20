from database.models import IssueLabel
from database.session import Session
from mappers.github import GitHubLabelMapper


async def create_label(body, issue_id, session=None):
    if session is None:
        session = Session()

    try:
        label = GitHubLabelMapper(body, issue_id)

        label = IssueLabel().fromdict(label.__dict__, allow_pk=True)

        session.add(label)
        session.flush()

    # TODO: add rollback expression
    except Exception as ex:
        print(ex)
