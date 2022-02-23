from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    lowest_set = (x & ~(x-1)) if (x & 1 == 0) else ((x+1) & ~(x))
    mask = lowest_set | (lowest_set >> 1)
    return x ^ mask

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
