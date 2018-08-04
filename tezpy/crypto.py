'''Crypto utilities

Implements various crypto utilities and wrap crypto libraries.
'''

import hashlib
import base58
import nacl


def hash(fun, data, hexd):
    if hexd:
        return fun(data).hexdigest()
    else:
        return fun(data).digest()


def sha256(data, hexd=False):
    return hash(hashlib.sha256, data, hexd)


def sha512(data, hexd=False):
    return hash(hashlib.sha512, data, hexd)


def b58encode_check(data, prefix):
    return base58.b58encode_check(prefix + data)


def b58decode_check(data, prefix):
    return base58.b58decode_check(data)[len(prefix):]


def randomKeys():
    priv = nacl.signing.SigningKey.generate()
    pub = priv.verify_key
    return (priv, pub)


def sign(sk, data):
    return sk.sign(data)


def verify(vk, data, signature):
    return vk.verify(data, signature)


def keyToHex(key):
    return key.encode(encoder=nacl.encoding.HexEncoder)

def keyFromHex(hexd, public=False):
    if public:
        return nacl.signing.VerifyKey(hexd, encoder=nacl.encoding.HexEncoder)
    else:
        return nacl.signing.SigningKey(hexd, encoder=nacl.encoding.HexEncoder)
