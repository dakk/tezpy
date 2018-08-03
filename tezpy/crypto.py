'''Crypto utilities

Implements various crypto utilities and wrap crypto libraries.
'''

import hashlib
import base58
import nacl


def hash(fun, data, hexd):
    if hexd:
        return fun(data).digest()
    else:
        return fun(data).hexdigest()


def sha256(data, hexd=False):
    return hash(hashlib.sha256, data, hexd)


def sha512(data, hexd=False):
    return hash(hashlib.sha256, data, hexd)


def b58encode_check(data, prefix):
    return base58.b58encode_check(prefix + data)


def b58decode_check(data, prefix):
    return base58.b58decode_check(data).slice(prefix)
