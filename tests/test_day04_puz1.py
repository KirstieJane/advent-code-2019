from day04.day04_puz1 import (valid_password, two_adj_dig_identical,
                              ascending_digits, six_digit,
                              count_valid_passwords, read_in_range)


def test_puzzle_ex_0():
    assert valid_password(122345), ("122345 is valid")


def test_puzzle_ex_1():
    assert valid_password(111123), ("111123 is valid")


def test_puzzle_ex_2():
    assert not valid_password(135679), ("135679 is not valid")


def test_puzzle_ex_3():
    assert valid_password(111111), ("111111 is valid")


def test_puzzle_ex_4():
    assert not valid_password(223450), ("223450 is not valid")


def test_puzzle_ex_5():
    assert not valid_password(123789), ("123789 is not valid")


def test_two_adj_dig_identical():
    assert two_adj_dig_identical(122345), (
           "122345 has two adjacent identical digits")
    assert two_adj_dig_identical(111123), (
           "111123 has two adjacent identical digits")
    assert not two_adj_dig_identical(135679), (
           "135679 does not have two adjacent identical digits")
    assert two_adj_dig_identical(111111), (
           "111111 has two adjacent identical digits")
    assert two_adj_dig_identical(223450), (
           "223450 has two adjacent identical digits")
    assert not two_adj_dig_identical(123789), (
           "123789 does not have two adjacent identical digits")
    assert not two_adj_dig_identical(1345), (
           "1345 does not have two adjacent identical digits")
    assert two_adj_dig_identical(9834566), (
           "9834566 has two adjacent identical digits")


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


def test_valid_password():
    assert valid_password(122345), (
           "122345 is a valid password")
    assert valid_password(111123), (
           "111123 is a valid password")
    assert not valid_password(135679), (
           "135679 is a valid password")
    assert valid_password(111111), (
           "111111 is a valid password")
    assert not valid_password(223450), (
           "223450 is not a valid password")
    assert not valid_password(123789), (
           "223450 is not a valid password")
    assert not valid_password(1345), (
           "1345 is not a valid password")
    assert not valid_password(9834566), (
           "9834566 is not a valid password")


def test_count_valid_passwords():

    assert count_valid_passwords([1230, 12983]) == 0
    assert count_valid_passwords([3453299, 5554556]) == 0
    assert count_valid_passwords([123780, 123788]) == 1, (
           "123788 is a valid password")
    assert count_valid_passwords([122325, 122350]) == 13, (
           "122333, 122334, 122335, 122336, 122337, 122338, 122339, " +
           "122344, 122345, 122346, 122347, 122348, 122349 " +
           "are valid passwords")
    assert count_valid_passwords([567775, 567795]) == 5, (
           "567777, 567778, 567779, 6567788, 567789 are valid passwords")


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
    assert n_valid == 511
