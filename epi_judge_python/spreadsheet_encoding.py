from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    result = 0

    for power, letter in enumerate(col[::-1]):
        result += (1 + ord(letter) - ord('A')) * pow(26, power)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
