from test_framework import generic_test


def reverse_bits(x: int) -> int:
    reversed_int = 0

    lookup = {
        0: 0,
        1: 2,
        2: 1,
        3: 3
    }

    bit_mask = 0b11
    mask_size = 2

    for i in reversed(range(64 // mask_size)):
        reversed_int |= lookup[x & bit_mask] << (mask_size * i)
        x >>= mask_size

    return reversed_int

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
