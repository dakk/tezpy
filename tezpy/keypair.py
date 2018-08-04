import crypto


class PublicKey:
    def __init__(self, key):
        self._key = key

    @staticmethod
    def fromHex(hexd):
        return PublicKey(crypto.keyFromHex(hexd, True))

    def verify(self, data, signature):
        return crypto.verify(self._key, data, signature)

    def toHex(self):
        return crypto.keyToHex(self._key)


class PrivateKey:
    def __init__(self, key):
        self._key = key

    @staticmethod
    def fromHex(hexd):
        return PrivateKey(crypto.keyFromHex(hexd, False))

    def sign(self, data):
        return crypto.sign(self._key, data)

    def toHex(self):
        return crypto.keyToHex(self._key)


class KeyPair:
    def __init__(self, priv, pub):
        self._pubKey = PublicKey(pub)
        self._privKey = PrivateKey(priv)

    @staticmethod
    def fromMnemonic(words):
        ''' Create a keypair from menmonic words '''
        return None

    @staticmethod
    def fromFundarising(email, password, words):
        ''' Create a keypair from fundraising data '''
        return None

    @staticmethod
    def generate():
        ''' Create a keypair from a random generated key '''
        (priv, pub) = crypto.randomKeys()
        return KeyPair(priv, pub)

    def address(self):
        ''' Returns the string representation of the keypair address '''
        hk = self._pubKey.toHex()
        return crypto.b58encode_check(hk, PREFIXES['tz1'])

    def public(self):
        ''' Returns the public key object '''
        return self._pubKey

    def sign(self, data):
        ''' Sign data '''
        return self._privKey.sign(data)

    def verify(self, data, signature):
        ''' Verify a signature '''
        return self._pubKey.verify(data, signature)
