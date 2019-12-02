#! /usr/bin/env python
import itertools as it


def run_opcode(code_list):
    """Run the opcode as determined by the values in code_list

    Before you enter the next loop, check to see if the opcode
    (the first number in the sequence of 4) is 99. If it is, then
    you can stop and return the code as it stands.

    Parameters
    ----------
    code_list : list
        The opcode
    """
    opcode, pos0, pos1, posout = 0, 0, 0, 0

    for i in range(len(code_list) // 4):

        # Read in the next 4 digits of the opcode
        opcode, pos0, pos1, posout = code_list[i*4:(i+1)*4:]

        # Add or multiply the values at positions 0 and 1 together
        if opcode == 1:
            output = code_list[pos0] + code_list[pos1]
        elif opcode == 2:
            output = code_list[pos0] * code_list[pos1]

        # Put the output value in the output position
        code_list[posout] = output

        # Get the next round's opcode
        opcode = code_list[(i+1)*4]

        # Don't do anything if the opcode is 99.
        # The code has stopped so you can stop!
        if opcode == 99:
            return code_list


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


def adjust_data(code_list, noun=12, verb=2):
    """Set the computer to a desired state by adjusting the noun and verb
    parameters.

    Parameters
    ----------
    code_list : list
        opcode as provided by advent of code
    noun : int, optional
        the first parameter (in position 1), by default 12
    verb : int, optional
        the second parameter (in position 2), by default 2
    """

    code_list[1] = noun
    code_list[2] = verb

    return code_list


def find_noun_verb(code_list, output=19690720):
    """Loop over lots of different pairs of nouns and verbs (the first two
    parameters given to an opcode) to find the given output (the first value
    in the whole list). Nouns and verbs are always between 0 and 99 inclusive

    Parameters
    ----------
    code_list : list
        the opcode as given by advent of code
    output : int, optional
        the first value in the list, by default 19690720
    """
    for noun, verb in it.product(range(100), range(100)):
        code_list = load_computer_data('day02/input.txt')
        code_list = adjust_data(code_list, noun=noun, verb=verb)
        code_list = run_opcode(code_list)

        if code_list[0] == output:
            return noun, verb, code_list


if __name__ == "__main__":
    """Load in the data, adjust it to the state before the computer caught fire,
    then run the opcode and print the value in position 0 to the screen.
    """
    code_list = load_computer_data('day02/input.txt')
    noun, verb, code_list = find_noun_verb(code_list, output=19690720)
    print(
        f'For output: {code_list[0]}\n'
        f'  Noun: {noun}\n'
        f'  Verb: {verb}\n'
        f'Answer to puzzle: {noun*100 + verb}')
