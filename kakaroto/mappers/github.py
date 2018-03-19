
class GitHubCardMapper(object):

    def __init__(self, body):
        super().__init__()
        self.id = body['id']
        self.project_id = get_project_id(body)
        self.note = body['note'] if body['note'] is not None else None
        self.created_by = body['creator']['id']


# TODO: method to retrieve project ID in database
#       move to appropiate file
def get_project_id(body):
    return 778903


class GitHubUserMapper(object):

    def __init__(self, body):
        super().__init__()
        self.id = body['id']
        self.login = body['login']
        self.html_url = body['html_url']


class GitHubCardMoveMapper(object):

    def __init__(self, body):
        super().__init__()
        self.board_column_id = body['column_id']
        self.card_id = body['id']


class GitHubIssueMapper(object):

    def __init__(self, body, card_id):
        super().__init__()
        self.id = body['id']
        self.card_id = card_id
        self.number = body['number']
        self.title = body['title']
        self.state = body['state']
        self.repository = body['repository_url']
        self.is_pull_request = True if 'pull_request' in body else False
        self.html_url = body['html_url']
        self.created_by = body['user']['id']
