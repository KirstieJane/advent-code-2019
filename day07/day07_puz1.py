#! /usr/bin/env python

import itertools as it


def run_opcode(code_list, programme_input=[0, 0], print_to_screen=True):
    """Run the opcode as determined by the values in code_list

    Before you enter the next loop, check to see if the opcode
    (the first number in the sequence) is 99. If it is, then
    you can stop and return the code as it stands.

    Parameters
    ----------
    code_list : list
        The opcode
    programme_input : list of ints
        The input to the programme, default [0, 0]
    print_to_screen : bool, optional
        Whether to print the output to screen or not, default True
    """
    # Start reading in the programme at position 0
    opcode_loc = 0  # Also known as the instruction pointer
    opcode = None
    output = None
    input_counter = 0

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
                                      programme_input=programme_input[input_counter]) # noqa

            # Increase the counter so you get the next programme input next
            # time
            input_counter += 1

            # Increase the opcode_loc by 2 to keep yourself moving forwards
            # through the code
            opcode_loc += 2

        if opcode == '04':
            # Return the output value if you have an opcode of 4
            code_list, output = apply_opcode4(code_list,
                                              opcode_loc,
                                              parameter_mode_dict)

            # Print the output value to screen
            if print_to_screen:
                print(f'Output value: {output}')

            # Increase the opcode_loc by 2 to keep yourself moving forwards
            # through the code
            opcode_loc += 2

        if opcode == '05':
            # Jump if true if you have an opcode of 5
            code_list, inc_steps = apply_opcode5(code_list,
                                                 opcode_loc,
                                                 parameter_mode_dict)

            # Increase the opcode_loc by inc_steps to keep yourself moving
            # forwards through the code
            opcode_loc += inc_steps

        if opcode == '06':
            # Jump if false if you have an opcode of 5
            code_list, inc_steps = apply_opcode6(code_list,
                                                 opcode_loc,
                                                 parameter_mode_dict)

            # Increase the opcode_loc by inc_steps to keep yourself moving
            # forwards through the code
            opcode_loc += inc_steps

        if opcode == '07':
            code_list, inc_steps = apply_opcode7(code_list,
                                                 opcode_loc,
                                                 parameter_mode_dict)

            # Increase the opcode_loc by inc_steps to keep yourself moving
            # forwards through the code
            opcode_loc += inc_steps

        if opcode == '08':
            # Assess whether the 1st parameter is equal to the 2nd parameter
            # if you have an opcode of 8
            code_list, inc_steps = apply_opcode8(code_list,
                                                 opcode_loc,
                                                 parameter_mode_dict)

            # Increase the opcode_loc by inc_steps to keep yourself moving
            # forwards through the code
            opcode_loc += inc_steps

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


def apply_opcode5(code_list, opcode_loc, parameter_mode_dict):
    """When you've determined that the opcode is 5 - which means to set the
    instruction pointer to the value from the second parameter if the first
    parameter is non zero - you can use this function to adjust code_list
    and return how many steps to increase the instruction pointer
    (aka opcode_loc).

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
    inc_steps : int
        The number of steps to increase the opcode_loc by for the next
        instruction
    """
    opcode, param1, param2 = code_list[opcode_loc:opcode_loc+3]

    # If the mode is 1 then the parameter should be interpreted as it stands.
    # If the mode is 0 then we need to get the value at that location in the
    # code list
    if parameter_mode_dict[1] == '0':
        param1 = code_list[param1]
    if parameter_mode_dict[2] == '0':
        param2 = code_list[param2]

    # If param1 is non-zero then set instruction pointer (opcode_loc) to the
    # value from param2
    if param1:
        new_opcode_loc = param2
        inc_steps = new_opcode_loc - opcode_loc
    else:
        inc_steps = 3

    return code_list, inc_steps


def apply_opcode6(code_list, opcode_loc, parameter_mode_dict):
    """When you've determined that the opcode is 6 - which means to set the
    instruction pointer to the value from the second parameter if the first
    parameter is zero - you can use this function to adjust code_list
    and return how many steps to increase the instruction pointer
    (aka opcode_loc).

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
    inc_steps : int
        The number of steps to increase the opcode_loc by for the next
        instruction
    """
    opcode, param1, param2 = code_list[opcode_loc:opcode_loc+3]

    # If the mode is 1 then the parameter should be interpreted as it stands.
    # If the mode is 0 then we need to get the value at that location in the
    # code list
    if parameter_mode_dict[1] == '0':
        param1 = code_list[param1]
    if parameter_mode_dict[2] == '0':
        param2 = code_list[param2]

    # If param1 is zero then set instruction pointer (opcode_loc) to the
    # value from param2
    if not param1:
        new_opcode_loc = param2
        inc_steps = new_opcode_loc - opcode_loc
    else:
        inc_steps = 3

    return code_list, inc_steps


def apply_opcode7(code_list, opcode_loc, parameter_mode_dict):
    """When you've determined that the opcode is 7 - which means to set the
    instruction pointer to 1 if the value from the first parameter is less than
    the value from the second parameter, otherwise set it to 0 - you can use
    this function to adjust code_list and return how many steps to increase the
    instruction pointer (aka opcode_loc).

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
    inc_steps : int
        The number of steps to increase the opcode_loc by for the next
        instruction
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

    # If param1 is less than param2 then set instruction pointer (opcode_loc)
    # to 1, otherwise set to 0
    if param1 < param2:
        code_list[param3] = 1
    else:
        code_list[param3] = 0

    # If you've overwritten the opcode for this instruction (the instruction
    # pointer) then don't increase the steps, otherwise increase by 4
    if param3 == opcode_loc:
        inc_steps = 0
    else:
        inc_steps = 4

    return code_list, inc_steps


def apply_opcode8(code_list, opcode_loc, parameter_mode_dict):
    """When you've determined that the opcode is 8 - which means to set the
    instruction pointer to 1 if the value from the first parameter is equal to
    the value from the second parameter, otherwise set it to 0 - you can use
    this function to adjust code_list and return how many steps to increase the
    instruction pointer (aka opcode_loc).

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
    inc_steps : int
        The number of steps to increase the opcode_loc by for the next
        instruction
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

    # If param1 is equal to param2 then set the value at the location given by
    # param3 to 1, otherwise set it to 0
    if param1 == param2:
        code_list[param3] = 1
    else:
        code_list[param3] = 0

    # If you've overwritten the opcode for this instruction (the instruction
    # pointer) then don't increase the steps, otherwise increase by 4
    if param3 == opcode_loc:
        inc_steps = 0
    else:
        inc_steps = 4

    return code_list, inc_steps


def run_code_through_five_amps(original_code,
                               phase_setting_seq,
                               amp_input=0,
                               print_to_screen=False):
    """Run the original code through the five amps described in day 7 part 1

    Parameters
    ----------
    original_code : list of ints
        The optcode provided by advent of code.
    phase_setting_seq : list of ints
        The phase settings for the 5 amplifiers
    amp_input : int, optional
        The input to the first amp, by default 0
    print_to_screen : bool, optional
        Whether to print the output to screen or not, default True

    Returns
    -------
    output : int
        The signal sent at the end of the five amps
    """

    for phase in phase_setting_seq:
        code_list, output = run_opcode(original_code,
                                       programme_input=[phase, amp_input],
                                       print_to_screen=print_to_screen)
        amp_input = output

    return output


def find_best_phase_setting_seq(original_code, amp_input=0):

    phase_setting_seq_dict = {}

    for phase_setting_seq in it.permutations(range(5)):
        output = run_code_through_five_amps(original_code,
                                            list(phase_setting_seq),
                                            amp_input=amp_input,
                                            print_to_screen=False)

        phase_setting_seq_dict[phase_setting_seq] = output

    best_phase_setting_seq = max(phase_setting_seq_dict,
                                 key=(lambda key: phase_setting_seq_dict[key]))

    return list(best_phase_setting_seq)


if __name__ == "__main__":
    """Load in the data, adjust it to the state before the computer caught fire,
    then run the opcode and print the value in position 0 to the screen.
    """
    original_code = load_computer_data('day07/input.txt')

    print('\n---- Day 7, Puzzle 1 ----')
    phase_setting_seq = find_best_phase_setting_seq(original_code,
                                                    amp_input=0)

    output = run_code_through_five_amps(original_code,
                                        phase_setting_seq,
                                        amp_input=0)

    print(f'Best sequence: {phase_setting_seq}')
    print(f'Max thruster signal: {output}')
