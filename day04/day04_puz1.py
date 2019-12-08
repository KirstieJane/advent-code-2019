#! /usr/bin/env python


def valid_password(password):
    """Check to see if the number provided is a 6 digit number, which has two
    identical adjacent digits, and in which all the numbers are ascending or
    staying the same.

    Parameters
    ----------
    password : int
        number to check whether it adheres to all the rules

    Returns
    -------
    is_valid: bool
        True if the password adheres to all the rules, False if not
    """

    # Start by assuming that the password is true.
    # This is going to get flipped to false at some point if
    # it fails one of the criteria
    is_valid = (six_digit(password)
                and two_adj_dig_identical(password)
                and ascending_digits(password))

    return is_valid


def six_digit(password):
    """Check if password has 6 digits

    Parameters
    ----------
    password : int
        password number

    Returns
    -------
    is_six_dig: bool
        True if password has six digits, False if not
    """

    # Test if password is a 6 digit number
    if password > 99999 and password < 1000000:
        return True
    else:
        return False


def two_adj_dig_identical(password):
    """Check to see if two adjacent digits in the password are the same

    Parameters
    ----------
    password : int
        password number

    Returns
    -------
    adj_dig_same: bool
        True if two adjacent digits are the same, False if not
    """

    # Convert password into list of 6 digits
    password_list = [int(d) for d in str(password)]

    # Set the boolean to False, we'll update this to True if there _are_
    # any adjacent values that are the same
    adj_dig_same = False

    # Loop through the digits and the ones just after them
    for a, b in zip(password_list, password_list[1:]):
        if a == b:
            adj_dig_same = True

    return adj_dig_same


def ascending_digits(password):
    """Check to see if each digit in the number is equal to or larger than
    the one before

    Parameters
    ----------
    password : int
        password number

    Returns
    -------
    ascending_dig: bool
        True if all digits are equal to or larger than the one before,
        False if not
    """

    # Convert password into list of 6 digits
    password_list = [int(d) for d in str(password)]

    # Set the boolean to True, we'll downgrade this to False if there _are_
    # any values that are smaller than the one before
    ascending_dig = True

    # Loop through the digits and the ones just after them
    for a, b in zip(password_list, password_list[1:]):
        if b < a:
            ascending_dig = False

    return ascending_dig


def count_valid_passwords(input_values):
    """Count the number of valid passwords within the given range

    Parameters
    ----------
    input_values : list
        lower and upper bounds of the range to check

    Returns
    -------
    valid_counter: int
        Number of valid passwords within the range
    """

    # Start a counter at 0
    valid_counter = 0

    for password in range(input_values[0], input_values[1]+1):
        if valid_password(password):
            valid_counter += 1

    return valid_counter


def read_in_range(fname):
    """Read in input file with the password range as provided.

    Parameters
    ----------
    fname : string
        File containing string provided by advent of code competition
    """

    # Create an empty list to hold the data
    input_values = []

    # Read in each line, and split by hypen
    with open(fname, 'r') as f:
        for line in f:
            input_values += line.split('-')

    # Convert all items to integer
    input_values = [int(item) for item in input_values]

    return input_values


if __name__ == "__main__":
    """Load in the data, adjust it to the state before the computer caught fire,
    then run the opcode and print the value in position 0 to the screen.
    """
    input_values = read_in_range('day04/input.txt')
    n_valid = count_valid_passwords(input_values)

    print('\n---- Day 4, Puzzle 1 ----')
    print(f'Number of valid passwords between {input_values[0]} '
          f'and {input_values[1]+1}: {n_valid}')
