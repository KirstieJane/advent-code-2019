#! /usr/bin/env python


def run_opcode(code_list, programme_input=1):
    """Run the opcode as determined by the values in code_list

    Before you enter the next loop, check to see if the opcode
    (the first number in the sequence) is 99. If it is, then
    you can stop and return the code as it stands.

    Parameters
    ----------
    code_list : list
        The opcode
    programme_input : int
        The input to the programme, default 1
    """
    # Start reading in the programme at position 0
    opcode_loc = 0
    opcode = None
    output = None

    while opcode != '99':

        # Get and parse the opcode
        code = code_list[opcode_loc]
        opcode, parameter_mode_dict = parse_opcode(code)

        if opcode == '01':
            # Add the appropriate values together if you have an opcode of 1
            code_list = apply_opcode1(code_list,
                                      opcode_loc,
                                      parameter_mode_dict)

            # Increase the opcode_loc by 4 to keep yourself moving forwards
            # through the code
            opcode_loc += 4

        if opcode == '02':
            # Multiply the appropriate values together if you have an opcode
            # of 2
            code_list = apply_opcode2(code_list,
                                      opcode_loc,
                                      parameter_mode_dict)

            # Increase the opcode_loc by 4 to keep yourself moving forwards
            # through the code
            opcode_loc += 4

        if opcode == '03':
            # Put the input value in the appropriate location if you have an
            # opcode of 3
            code_list = apply_opcode3(code_list,
                                      opcode_loc,
                                      programme_input=programme_input)

            # Increase the opcode_loc by 2 to keep yourself moving forwards
            # through the code
            opcode_loc += 2

        if opcode == '04':
            # Return the output value if you have an opcode of 4
            code_list, output = apply_opcode4(code_list,
                                              opcode_loc,
                                              parameter_mode_dict)

            # Print the output value to screen
            print(f'Output value: {output}')

            # Increase the opcode_loc by 2 to keep yourself moving forwards
            # through the code
            opcode_loc += 2

            # If the output is not 0 then check that it is followed by a 99
            if output != 0:
                check_next_opcode_99(opcode_loc, code_list)

    return code_list, output


def load_computer_data(fname):
    """Read in input file with the computer's opcode as provided.

    Parameters
    ----------
    fname : string
        File provided by advent of code competition
    """

    # Create empty code list
    code_list = []

    # Read in each line, and split by comma
    with open(fname, 'r') as f:
        for line in f:
            code_list += line.split(',')

    # Convert all items to integer
    code_list = [int(item) for item in code_list]

    return code_list


def parse_opcode(code):
    """Each opcode is up to 5 digits long. The two on the furthest right
    contain the instruction, and then the 3 on the left (reading from right
    to left) indicate the mode (position or immediate) for each of the
    parameters.

    This function converts the number to a 0 padded string and then splits up
    the 5 digits into the opcode and parameter modes.

    Parameters
    ----------
    code : int
        instruction as integer that is up to 5 digits long

    Returns
    -------
    opcode : str
        two digit string corresponding to an instruction
    parameter_mode_dict : dict
        dictionary containing the parameter mode for each of the opcode
        parameters
    """

    code = f'{code:05}'

    opcode = code[3:5]

    parameter_mode_dict = {1: code[2], 2: code[1], 3: code[0]}

    return opcode, parameter_mode_dict


# Define Python user-defined exceptions
# Adapted from https://www.programiz.com/python-programming/user-defined-exception # noqa
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ForbiddenValueError(Error):
    """Raised when the opcode mode is not permitted"""
    pass


def apply_opcode1(code_list, opcode_loc, parameter_mode_dict):
    """When you've determined that the opcode is 1 - which means to add the
    following two numbers (or the values at the position of those two numbers,
    depending on the parameter mode) then you can use this function to adjust
    code_list.

    Parameters
    ----------
    code_list : list
        The whole programme
    opcode_loc : int
        The index of the opcode in code_list
    parameter_mode_dict : dict
        A dictionary indicating for the following 3 values after an opcode of 1
        whether they should be considered in position (0) or immediate (1)
        modes

    Returns
    -------
    code_list : list
        The whole programme
    """

    opcode, param1, param2, param3 = code_list[opcode_loc:opcode_loc+4]

    # If the mode is 1 then the parameter should be interpreted as it stands.
    # If the mode is 0 then we need to get the value at that location in the
    # code list
    if parameter_mode_dict[1] == '0':
        param1 = code_list[param1]
    if parameter_mode_dict[2] == '0':
        param2 = code_list[param2]

    # The parameter mode for the 3rd parameter (which is the location that
    # the answer will be stored) should never be anything other than 0, so
    # we're going to raise an error if it is
    if parameter_mode_dict[3] != '0':
        print('Something has gone wrong! ' +
              'The 3rd parameter should never be anything other than 0')
        raise ForbiddenValueError

    # Now lets actually do what the opcode says: add param1 and param2 and
    # put the value at param3
    code_list[param3] = param1 + param2

    return code_list


def apply_opcode2(code_list, opcode_loc, parameter_mode_dict):
    """When you've determined that the opcode is 2 - which means to multiply
    the following two numbers (or the values at the position of those two
    numbers, depending on the parameter mode) then you can use this function to
    adjust code_list.

    Parameters
    ----------
    code_list : list
        The opcode
    opcode_loc : int
        The index of the opcode in code_list
    parameter_mode_dict : dict
        A dictionary indicating for the following 3 values after an opcode of 2
        whether they should be considered in position (0) or immediate (1)
        modes

    Returns
    -------
    code_list : list
        The whole programme
    """

    opcode, param1, param2, param3 = code_list[opcode_loc:opcode_loc+4]

    # If the mode is 1 then the parameter should be interpreted as it stands.
    # If the mode is 0 then we need to get the value at that location in the
    # code list
    if parameter_mode_dict[1] == '0':
        param1 = code_list[param1]
    if parameter_mode_dict[2] == '0':
        param2 = code_list[param2]

    # The parameter mode for the 3rd parameter (which is the location that
    # the answer will be stored) should never be anything other than 0, so
    # we're going to raise an error if it is
    if parameter_mode_dict[3] != '0':
        print('Something has gone wrong! ' +
              'The 3rd parameter should never be anything other than 0')
        raise ForbiddenValueError

    # Now lets actually do what the opcode says: multiply param1 and param2 and
    # put the value at param3
    code_list[param3] = param1 * param2

    return code_list


def apply_opcode3(code_list, opcode_loc, programme_input=1):
    """When you've determined that the opcode is 3 - which means to take an
    input value and store it in the location of its only parameter then you can
    use this function to
    adjust code_list.

    Parameters
    ----------
    code_list : list
        The opcode
    opcode_loc : int
        The index of the opcode in code_list
    programme_input : int
        input value, default 1

    Returns
    -------
    code_list : list
        The whole programme
    """

    opcode, param1 = code_list[opcode_loc:opcode_loc+2]

    # Now lets actually do what the opcode says: put the input value at the
    # location given by param1
    code_list[param1] = programme_input

    return code_list


def apply_opcode4(code_list, opcode_loc, parameter_mode_dict):
    """When you've determined that the opcode is 4 - which means to return a
    value in the location of its only parameter as an output - you can use this
    function to adjust code_list.

    Parameters
    ----------
    code_list : list
        The opcode
    opcode_loc : int
        The index of the opcode in code_list
    parameter_mode_dict : dict
        A dictionary indicating for the following value after an opcode of 3
        whether they should be considered in position (0) or immediate (1)
        modes

    Returns
    -------
    code_list : list
        The whole programme
    output : int
        The value in the location determined by the parameter of the opcode
    """

    opcode, param1 = code_list[opcode_loc:opcode_loc+2]

    # If the mode is 1 then the parameter should be interpreted as it stands.
    # If the mode is 0 then we need to get the value at that location in the
    # code list
    if parameter_mode_dict[1] == '0':
        param1 = code_list[param1]

    # Return that value as an output
    output = param1

    return code_list, output


def check_next_opcode_99(opcode_loc, code_list):
    # A non-zero output value should only occur *right* before
    # the programme ends.
    # So we're going to check that the next opcode is 99, and raise
    # an error if not
    code = code_list[opcode_loc]
    opcode, parameter_mode_dict = parse_opcode(code)

    if not opcode == '99':
        print(f'NEXT OPCODE: {opcode}')
        print('Something has gone wrong! ' +
              'There is a non-zero output that is not followed by a halt :(')
        raise ForbiddenValueError


if __name__ == "__main__":
    """Load in the data, adjust it to the state before the computer caught fire,
    then run the opcode and print the value in position 0 to the screen.
    """
    code_list = load_computer_data('day05/input.txt')

    print('\n---- Day 5, Puzzle 1 ----')
    code_list, output = run_opcode(code_list, programme_input=1)
