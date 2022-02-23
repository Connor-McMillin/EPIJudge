from test_framework import generic_test


def parity(x: int) -> int:
    lookup = {
        0: 0,
        1: 1,
        2: 1,
        3: 0
    }

    result = 0
    while x:
        result ^= lookup[x & 0b11]
        x >>= 2

    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
