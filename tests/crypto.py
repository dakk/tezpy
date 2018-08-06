import unittest
from tezpy import crypto, constants


class TestHash(unittest.TestCase):
    def test_sha256_hex(self):
        self.assertEqual(crypto.sha256(
            b'FOO', True), '9520437ce8902eb379a7d8aaa98fc4c94eeb07b6684854868fa6f72bf34b0fd3')

    def test_sha256(self):
        self.assertEqual(crypto.sha256(
            b'FOO'), b'\x95 C|\xe8\x90.\xb3y\xa7\xd8\xaa\xa9\x8f\xc4\xc9N\xeb\x07\xb6hHT\x86\x8f\xa6\xf7+\xf3K\x0f\xd3')

    def test_sha512_hex(self):
        self.assertEqual(crypto.sha512(
            b'FOO', True), '9840f9826bba3ddfc3c4872884f51dcbe915a2d42c6a4d0d59ce564e7fe541f15b9a4271554065379709932bc99a71d85f05aacd62457fce5fd131f847de99ec')

    def test_sha512(self):
        self.assertEqual(crypto.sha512(
            b'FOO'), b'\x98@\xf9\x82k\xba=\xdf\xc3\xc4\x87(\x84\xf5\x1d\xcb\xe9\x15\xa2\xd4,jM\rY\xceVN\x7f\xe5A\xf1[\x9aBqU@e7\x97\t\x93+\xc9\x9aq\xd8_\x05\xaa\xcdbE\x7f\xce_\xd11\xf8G\xde\x99\xec')

    def test_blake2b32(self):
        self.assertEqual(crypto.blake2b(
            32, b'FOO'), b"\xc6\xac\xa9\x16\xa3\xea\xb4bp\x84\xef{\xf8\x95\x88\x8e\xb8\x93\xa6\xf0\xab'P\xcb\xfb\xb9K\x1bt\xd5\\\xc7")
        self.assertEqual(crypto.blake2b(
            32, b'FOO', True), 'c6aca916a3eab4627084ef7bf895888eb893a6f0ab2750cbfbb94b1b74d55cc7')

    def test_blake2b20(self):
        self.assertEqual(crypto.blake2b(
            20, b'FOO'), b'\xdb\xc3\x93>f\xf7\xe5\xf7u\x9e\x02\x1bI~\x97\xa9x\x06\xc1\x01')
        self.assertEqual(crypto.blake2b(20, b'FOO', True),
                         'dbc3933e66f7e5f7759e021b497e97a97806c101')


class TestBase58Check(unittest.TestCase):
    def test_base58c_encode(self):
        self.assertEqual(crypto.b58encode_check(crypto.blake2b(
            20, b'FOO'), constants.PREFIXES['tz1']), b'tz1fg2xvxfwADx1yR4ZZgf33nFSNUUnamwVF')

        self.assertEqual(crypto.b58encode_check(
            b'S\xf0\xe1\x11\xf0\x86[\xaa\xaa\xacoSR\x9d\xdf\x882\x8a|]', constants.PREFIXES['tz1']), b'tz1THsLcunLo8CmDm9f2y1xHuXttXZCpyFnq')

        self.assertEqual(crypto.b58encode_check(b'\xef\xc7\xa1\x8e&\x16\x84\xb1}\n-\xe1\x085Fi\xc3H\x02>',
                                                constants.PREFIXES['KT']), b'KT1WScDDtweGCKQioUgHi7WHTc9TVsVyyM3b')

    def test_base58c_decode(self):
        self.assertEqual(crypto.b58decode_check(
            b'tz1fg2xvxfwADx1yR4ZZgf33nFSNUUnamwVF', constants.PREFIXES['tz1']), crypto.blake2b(20, b'FOO'))

        self.assertEqual(crypto.b58decode_check(
            b'tz1THsLcunLo8CmDm9f2y1xHuXttXZCpyFnq', constants.PREFIXES['tz1']), b'S\xf0\xe1\x11\xf0\x86[\xaa\xaa\xacoSR\x9d\xdf\x882\x8a|]')

        self.assertEqual(crypto.b58decode_check(
            b'KT1WScDDtweGCKQioUgHi7WHTc9TVsVyyM3b', constants.PREFIXES['KT']), b'\xef\xc7\xa1\x8e&\x16\x84\xb1}\n-\xe1\x085Fi\xc3H\x02>')


if __name__ == '__main__':
    unittest.main()
