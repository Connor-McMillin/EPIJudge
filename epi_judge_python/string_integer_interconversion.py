from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"

    set_negative = x < 0

    if set_negative:
        x *= -1

    result = ""

    while x > 0:
        to_add = x % 10
        x = x // 10
        result = str(to_add) + result

    if set_negative:
        return "-" + result
    else:
        return  result

def string_to_int(s: str) -> int:
    result = 0

    set_negative = s.startswith("-")
    s = s.strip('+-')

    for num in s:
        result *= 10
        result += ord(num) - ord("0")

    if set_negative:
        return result * -1
    else:
        return result


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
