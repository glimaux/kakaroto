from requests import request

from config import GITHUB


headers = {
    'Authorization': 'token ' + GITHUB['SECRET_KEY'],
    'Cache-Control': "no-cache"
}


async def get_issue(url, headers=headers):

    try:
        response = request('GET', url, headers=headers)

        return response.json()

    except Exception as ex:
        print(ex)
