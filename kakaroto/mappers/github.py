
class GitHubCardMapper(object):

    def __init__(self, body):
        super().__init__()
        self.id = body['project_card']['id']
        self.project_id = get_project_id(body)
        self.note = body['project_card']['note'] if body['project_card']['note'] is not None else None
        self.created_by = body['project_card']['creator']['id']


# TODO: method to retrieve project ID in database
def get_project_id(body):
    return 778903


class GitHubUserMapper(object):

    def __init__(self, body):
        super().__init__()
        self.id = body['id']
        self.login = body['login']
        self.html_url = body['html_url']
