import requests


class Node:
    def __init__(self, uri, rest=True):
        self._uri = uri
        self._rest = rest

    def _request(self, endpoint, data=None):
        if self._rest:
            if data:
                return requests.post(self._uri + endpoint, data)
            else:
                return requests.get(self._uri + endpoint)

    def head(self):
        return self._request('/blocks/head')
