import unittest
from tezpy import crypto

class TestHash(unittest.TestCase):
    def test_sha256_hex(self):
        self.assertEqual(crypto.sha256(b'FOO', True), '9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3')

    def test_sha256(self):
        self.assertEqual(crypto.sha256(b'FOO'), b'\x95 C|\xe8\x90.\xb3y\xa7\xd8\xaa\xa9\x8f\xc4\xc9N\xeb\x07\xb6hHT\x86\x8f\xa6\xf7+\xf3K\x0f\xd3')

    def test_sha512_hex(self):
        self.assertEqual(crypto.sha512(b'FOO', True), '9840f9826bba3ddfc3c4872884f51dcbe915a2d42c6a4d0d59ce564e7fe541f15b9a4271554065379709932bc99a71d85f05aacd62457fce5fd131f847de99ec')

    def test_sha512(self):
        self.assertEqual(crypto.sha512(b'FOO'), b'\x98@\xf9\x82k\xba=\xdf\xc3\xc4\x87(\x84\xf5\x1d\xcb\xe9\x15\xa2\xd4,jM\rY\xceVN\x7f\xe5A\xf1[\x9aBqU@e7\x97\t\x93+\xc9\x9aq\xd8_\x05\xaa\xcdbE\x7f\xce_\xd11\xf8G\xde\x99\xec')


class TestBase58Check(unittest.TestCase):
    def test_base58c_encode(self):
        self.assertEqual(crypto.b58encode_check(crypto.sha256(b'FOO'), bytes([6, 161, 159])), b'')

    def test_base58c_decode(self):
        pass



if __name__ == '__main__':
	unittest.main()
