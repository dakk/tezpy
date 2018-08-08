import requests
import math
import constants


class Node:
    def __init__(self, uri, rest=True):
        self._uri = uri
        self._rest = rest

    def _request(self, endpoint, data=None):
        if self._rest:
            if data:
                return requests.post(self._uri + endpoint, data).json()
            else:
                return requests.get(self._uri + endpoint).json()

    def getHead(self):
        return self._request('/blocks/head')

    def getHeadHash(self):
        return self._request('/blocks/head/hash')

    def getCurrentCycle(self):
        return math.floor(self._request('/chains/main/blocks/head/header')['level'] / constants.BLOCKS_PER_CYCLE)

    def getBalance(self, address):
        return self._request('/chains/main/blocks/head/context/contracts/' + address + '/balance')

    def getBlockHashByIndex(self, idx):
        head_level = self._request('/chains/main/blocks/head/header')['level']
        return self._request('/chains/main/blocks/head~' + str(head_level - idx) + '/header')['hash']

    def getBakingRights(self, cycle, delegate):
        return self._request("/chains/main/blocks/head/helpers/baking_rights?delegate=" + delegate + '&cycle=' + str(cycle))

    def getEndorsmentRights(self, cycle, delegate):
        return self._request("/chains/main/blocks/head/helpers/endorsment_rights?delegate=" + delegate + '&cycle=' + str(cycle))

    def getSnapshot(self, cycle, delegate):
        snapshot_block_offset = self._request(
            '/chains/main/blocks/head/context/raw/json/rolls/owner/snapshot/' + str(cycle))[0]

        # Then multiply the result with 256 and sum the cycle index, we get the block of the snapshot
        snapshot_block_index = (
            (cycle-constants.PRESERVED_CYCLES-2)*4096)+((snapshot_block_offset+1)*256)

        # Get the delegate information for the given snapshot
        block_hash = self.getBlockHashByIndex(snapshot_block_index)
        return self._request("/chains/main/blocks/" + block_hash + "/context/delegates/" + delegate)

    def forgeOperations(self, ops):
        ''' Forge an operation and return opbytes '''
        head = self.getHead()
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
