import requests


class HTTP:

    def __init__(self, token, url):
        self.headers = {
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.api+json"
        }
        self.r = None
        self.response = self.make_request(url)
        self.json = self.response.json()

    def make_request(self, endpoint):
        self.r = requests.get(endpoint, headers=self.headers)
        return self.r
