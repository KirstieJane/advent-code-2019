from day02.day02_puz2 import (run_opcode, load_computer_data, adjust_data,
                              find_noun_verb)


def test_puzzle_ex_0():
    assert run_opcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99], (
           "Should be 2,0,0,0,99")


def test_puzzle_ex_1():
    assert run_opcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99], (
           "Should be 2,3,0,6,99")


def test_puzzle_ex_2():
    assert run_opcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801], (
           "Should be 2,4,4,5,99,9801")


def test_puzzle_ex_3():
    assert (run_opcode([1, 1, 1, 4, 99, 5, 6, 0, 99])
            == [30, 1, 1, 4, 2, 5, 6, 0, 99]), (
           "Should be 30,1,1,4,2,5,6,0,99")


def create_test_data():
    """Use the longest example for our test data

    Returns
    -------
    list
        opcode from the examples
    """
    test_list = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    return test_list


def test_input():
    """Check the length and data type (int) for test data
    and the input.txt file
    """
    test_list = create_test_data()
    assert len(test_list) == 9
    code_list = load_computer_data('day02/input.txt')
    assert len(code_list) == 145
    assert all(isinstance(item, int) for item in test_list)
    assert all(isinstance(item, int) for item in code_list)


def test_adjust_data():
    test_list = create_test_data()
    test_list = adjust_data(test_list)
    assert test_list[1] == 12
    assert test_list[2] == 2


def test_find_noun_verb(output=7594646):
    """We know from puzzle 1 that the output is 7594646 when we give it the
    following two parameters (noun: 12 and verb: 2).

    Parameters
    ----------
    code_list : list
        the opcode as provided by advent of code
    output : int, optional
        the output of the code, the first value in the list, by default 7594646
    """
    # Test first by setting the values explicitly and checking you get the
    # set output value
    code_list = load_computer_data('day02/input.txt')
    code_list = adjust_data(code_list, noun=12, verb=2)
    code_list = run_opcode(code_list)
    assert code_list[0] == output

    # Next test by finding the right values for the noun and verb when you
    # search to match the output
    code_list = load_computer_data('day02/input.txt')
    noun, verb, code_list = find_noun_verb(code_list, output=output)
    assert noun == 12
    assert verb == 2
    assert code_list[0] == output


def test_integration():
    """I know the correct answer, lets check that the code gives me it!
    """
    code_list = load_computer_data('day02/input.txt')
    noun, verb, code_list = find_noun_verb(code_list, output=19690720)
    assert noun == 33
    assert verb == 76
    assert code_list[0] == 19690720
    puzzle_answer = noun*100 + verb
    assert puzzle_answer == 3376
