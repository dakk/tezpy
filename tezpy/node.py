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

    def headHash(self):
        return self._request('/blocks/head/hash')

    def balance(self, address):
        return self._request('/chains/main/blocks/head/context/contracts/' + address + '/balance')

    def forgeOperations(self, ops):
        ''' Forge an operation and return opbytes '''
        head = self.head()
        opobject = {
            "branch": head['hash'],
            "contents": list(map(lambda op: op.toJson(), ops))
        }
        opbytes = self._request('/chains/'+head['chain_id']+'/blocks/' +
                                head['hash']+'/helpers/forge/operations', opobject)
        opobject['protocol'] = head.protocol
        return opbytes, opobject

    def injectOperation(self, sopbytes):
        self._request('/injection/operation', sopbytes)
