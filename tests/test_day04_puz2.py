from day04.day04_puz2 import (valid_password, exactly_two_adj_dig_identical,
                              ascending_digits, six_digit,
                              count_valid_passwords, read_in_range)


def test_puzzle_ex_0():
    assert valid_password(122345), ("122345 is valid")


def test_puzzle_ex_1():
    assert not valid_password(111123), ("111123 is not valid")


def test_puzzle_ex_2():
    assert not valid_password(135679), ("135679 is not valid")


def test_puzzle_ex_3():
    assert not valid_password(111111), ("111111 is not valid")


def test_puzzle_ex_4():
    assert not valid_password(223450), ("223450 is not valid")


def test_puzzle_ex_5():
    assert not valid_password(123789), ("123789 is not valid")


def test_puzzle_ex_6():
    assert valid_password(112233), ("112233 is valid")


def test_puzzle_ex_7():
    assert not valid_password(123444), ("123444 is not valid")


def test_puzzle_ex_8():
    assert valid_password(111122), ("111122 is valid")


def test_exactly_two_adj_dig_identical():
    assert exactly_two_adj_dig_identical(122345), (
           "122345 has exactly two adjacent identical digits")
    assert not exactly_two_adj_dig_identical(111123), (
           "111123 does not have exactly two adjacent identical digits")
    assert not exactly_two_adj_dig_identical(135679), (
           "135679 does not have exactly two adjacent identical digits")
    assert not exactly_two_adj_dig_identical(111111), (
           "111111 does not have exactly two adjacent identical digits")
    assert exactly_two_adj_dig_identical(223450), (
           "223450 has exactly two adjacent identical digits")
    assert not exactly_two_adj_dig_identical(123789), (
           "123789 does not have exactly two adjacent identical digits")
    assert not exactly_two_adj_dig_identical(1345), (
           "1345 does not have exactly two adjacent identical digits")
    assert exactly_two_adj_dig_identical(9834566), (
           "9834566 has exactly two adjacent identical digits")
    assert exactly_two_adj_dig_identical(112233), (
           "112233 has exactly two adjacent identical digits")
    assert not exactly_two_adj_dig_identical(123444), (
           "123444 does not have exactly two adjacent identical digits")
    assert exactly_two_adj_dig_identical(111122), (
           "111122 has exactly two adjacent identical digits")


def test_ascending_digits():
    assert ascending_digits(122345), (
           "all digits in 122345 are ascending or the same")
    assert ascending_digits(111123), (
           "all digits in 111123 are ascending or the same")
    assert ascending_digits(135679), (
           "all digits in 135679 are ascending or the same")
    assert ascending_digits(111111), (
           "all digits in 111111 are ascending or the same")
    assert not ascending_digits(223450), (
           "not all digits in 223450 are ascending or the same")
    assert ascending_digits(123789), (
           "all digits in 123789 are ascending or the same")
    assert ascending_digits(1345), (
           "all digits in 1345 are ascending or the same")
    assert not ascending_digits(9834566), (
           "not all digits in 9834566 are ascending or the same")
    assert ascending_digits(112233), (
           "all digits in 112233 are ascending or the same")
    assert ascending_digits(123444), (
           "all digits in 123444 are ascending or the same")
    assert ascending_digits(111122), (
           "all digits in 111122 are ascending or the same")


def test_six_digit():
    assert six_digit(122345), (
           "there are 6 digits in 122345")
    assert six_digit(111123), (
           "there are 6 digits in 111123")
    assert six_digit(135679), (
           "there are 6 digits in 135679")
    assert six_digit(111111), (
           "there are 6 digits in 111111")
    assert six_digit(223450), (
           "there are 6 digits in 223450")
    assert six_digit(123789), (
           "there are 6 digits in 123789")
    assert not six_digit(1345), (
           "there are 4 digits in 1345")
    assert not six_digit(9834566), (
           "there are 7 digits in 9834566")
    assert six_digit(112233), (
           "there are 6 digits in 123444")
    assert six_digit(123444), (
           "there are 6 digits in 123444")
    assert six_digit(111122), (
           "there are 6 digits in 111122")


def test_valid_password():
    assert valid_password(122345), (
           "122345 is a valid password")
    assert not valid_password(111123), (
           "111123 is a valid password")
    assert not valid_password(135679), (
           "135679 is not a valid password")
    assert not valid_password(111111), (
           "111111 is not a valid password")
    assert not valid_password(223450), (
           "223450 is not a valid password")
    assert not valid_password(123789), (
           "223450 is not a valid password")
    assert not valid_password(1345), (
           "1345 is not a valid password")
    assert not valid_password(9834566), (
           "9834566 is not a valid password")
    assert valid_password(112233), (
           "122345 is a valid password")
    assert not valid_password(123444), (
           "123444 is not a valid password")
    assert valid_password(111122), (
           "111122 is a valid password")


def test_count_valid_passwords():

    assert count_valid_passwords([1230, 12983]) == 0
    assert count_valid_passwords([3453299, 5554556]) == 0
    assert count_valid_passwords([123780, 123788]) == 1, (
           "123788 is a valid password")
    assert count_valid_passwords([122325, 122350]) == 13, (
           "122333, 122334, 122335, 122336, 122337, 122338, 122339, " +
           "122344, 122345, 122346, 122347, 122348, 122349 " +
           "are valid passwords")
    assert count_valid_passwords([567775, 567795]) == 2, (
           "567788, 567789 are valid passwords")


def test_input_values():

    input_values = [122345, 122350]
    assert list(range(input_values[0],
                      input_values[1]+1)) == [122345, 122346, 122347, 122348,
                                              122349, 122350]

    input_values = read_in_range('day04/input.txt')
    assert len(range(input_values[0],
                     input_values[1]+1)) == 461120


def test_read_in_range():

    assert read_in_range('day04/input.txt') == [359282, 820401]


def test_integration():
    """I know the correct answer, lets check that the code gives me it!
    """
    input_values = read_in_range('day04/input.txt')
    n_valid = count_valid_passwords(input_values)
    assert n_valid == 316
