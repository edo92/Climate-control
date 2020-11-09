import requests
import json


class Request:
    def __init__(self, url):
        self.url = url
        self.headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        }

    def get(self, route):
        return requests.get(url=self.url + route, headers=self.headers)

    def post(self, data):
        requests.post(url=self.url, data=json.dumps(
            data), headers=self.headers)
