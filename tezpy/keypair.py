PREFIXES = {
    'tz1': [6, 161, 159],
    'tz2': [6, 161, 161],
    'tz3': [6, 161, 164],
    'KT': [2, 90, 121],

    'edpk': [13, 15, 37, 217],
    'edsk2': [13, 15, 58, 7]
}

"""
  spsk: new Uint8Array([17, 162, 224, 201]),
  p2sk: new Uint8Array([16,81,238,189]),
  
  sppk: new Uint8Array([3, 254, 226, 86]),
  p2pk: new Uint8Array([3, 178, 139, 127]),
  
  edsk: new Uint8Array([43, 246, 78, 7]),
  edsig: new Uint8Array([9, 245, 205, 134, 18]),
  spsig1: new Uint8Array([13, 115, 101, 19, 63]),
  p2sig: new Uint8Array([54, 240, 44, 52]),
  sig: new Uint8Array([4, 130, 43]),
  
  Net: new Uint8Array([87, 82, 0]),
  nce: new Uint8Array([69, 220, 169]),
  b: new Uint8Array([1,52]),
  o: new Uint8Array([5, 116]),
  Lo: new Uint8Array([133, 233]),
  LLo: new Uint8Array([29, 159, 109]),
  P: new Uint8Array([2, 170]),
  Co: new Uint8Array([79, 179]),
  id: new Uint8Array([153, 103]),
}
"""


class PublicKey:
    def verify(self, data, signature):
        return False


class PrivateKey:
    def sign(self, data):
        return None


class KeyPair:
    def __init__(self):
        self._pubKey = None
        self._privKey = None

    @staticmethod
    def fromMnemonic(words):
        ''' Create a keypair from menmonic words '''
        return None

    @staticmethod
    def fromFundarising(email, password, words):
        ''' Create a keypair from fundraising data '''
        return None

    def sign(self, data):
        ''' Sign data '''
        return self._privKey.sign(data)

    def verify(self, data, signature):
        ''' Verify a signature '''
        return self._pubKey.verify(data, signature)
