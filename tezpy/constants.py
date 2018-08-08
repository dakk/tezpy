PRESERVED_CYCLES = 5
BLOCK_REWARD = 16 * 1000000.
ENDORSMENT_REWARD = 2 * 1000000.
BLOCKS_PER_CYCLE = 4096

PREFIXES = {
    'tz1': bytes([6, 161, 159]),
    'tz2': bytes([6, 161, 161]),
    'tz3': bytes([6, 161, 164]),
    'KT': bytes([2, 90, 121]),

    'edpk': bytes([13, 15, 37, 217]),
    'edsk2': bytes([13, 15, 58, 7]),

    'spsk': bytes([17, 162, 224, 201]),
    'p2sk': bytes([16, 81, 238, 189]),
    'sppk': bytes([3, 254, 226, 86]),
    'p2pk': bytes([3, 178, 139, 127]),

    'edsk': bytes([43, 246, 78, 7]),
    'edsig': bytes([9, 245, 205, 134, 18]),
    'spsig1': bytes([13, 115, 101, 19, 63]),
    'p2sig': bytes([54, 240, 44, 52]),
    'sig': bytes([4, 130, 43]),

    'Net': bytes([87, 82, 0]),
    'nce': bytes([69, 220, 169]),
    'b': bytes([1, 52]),
    'o': bytes([5, 116]),
    'Lo': bytes([133, 233]),
    'LLo': bytes([29, 159, 109]),
    'P': bytes([2, 170]),
    'Co': bytes([79, 179]),
    'id': bytes([153, 103]),
}
