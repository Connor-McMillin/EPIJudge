from test_framework import generic_test


def swap_bits(x, i, j):
    ith_bit = (x >> i) & 1
    jth_bit = (x >> j) & 1

    if ith_bit == jth_bit:
        return x
    else:
        return x ^ (1 << i | 1 << j)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
