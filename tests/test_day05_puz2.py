from day05.day05_puz2 import (run_opcode, load_computer_data, parse_opcode,
                              apply_opcode1, apply_opcode2,
                              apply_opcode3, apply_opcode4,
                              apply_opcode5, apply_opcode6,
                              apply_opcode7, apply_opcode8,
                              ForbiddenValueError)
import pytest


def test_puzzle_ex_0():
    code_list, output = run_opcode([1002, 4, 3, 4, 33])
    assert code_list == [1002, 4, 3, 4, 99], (
           "Should be 1002,4,3,4,99")
    assert output is None


def test_puzzle_ex_1():
    code_list, output = run_opcode([1101, 100, -1, 4, 0])
    assert code_list == [1101, 100, -1, 4, 99], (
           "Should be 1101,100,-1,4,99")
    assert output is None


def test_puzzle_ex_2():
    code_list, output = run_opcode([3, 0, 4, 0, 99], programme_input=1)
    assert code_list == [1, 0, 4, 0, 99], (
           "Should be 1,0,4,0,99")
    assert output == 1

    code_list, output = run_opcode([3, 0, 4, 0, 99], programme_input=20)
    assert code_list == [20, 0, 4, 0, 99], (
           "Should be 20,0,4,0,99")
    assert output == 20


def test_puzzle_ex_3():
    code_list, output = run_opcode([3, 0, 104, 0, 99], programme_input=1)
    assert code_list == [1, 0, 104, 0, 99], (
           "Should be 1,0,104,0,99")
    assert output == 0


def test_puzzle_ex_4():
    code_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    programme_input = 1
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert code_list == [3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8]
    assert output == 0

    code_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    programme_input = 8
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert code_list == [3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8]
    assert output == 1

    code_list = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    programme_input = 13
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert code_list == [3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8]
    assert output == 0


def test_puzzle_ex_5():

    code_list = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    programme_input = 3
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 1

    code_list = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    programme_input = 8
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 0

    code_list = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    programme_input = 13
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 0


def test_puzzle_ex_6():

    code_list = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    programme_input = 3
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 0

    code_list = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    programme_input = 8
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 1

    code_list = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    programme_input = 13
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 0


def test_puzzle_ex_7():

    code_list = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    programme_input = 3
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 1

    code_list = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    programme_input = 8
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 0

    code_list = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    programme_input = 13
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 0


def test_puzzle_ex_8():
    """
    Opcode 5 is jump-if-true: if the first parameter is non-zero,
        it sets the instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
    Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
        instruction pointer to the value from the second parameter.
        Otherwise, it does nothing.
    """
    code_list = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    programme_input = 0
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert code_list == [3, 12, 6, 12, 15, 1, 13, 14, 13, 4,
                         13, 99, 0, 0, 1, 9]
    assert output == 0

    code_list = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    programme_input = 3
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert code_list == [3, 12, 6, 12, 15, 1, 13, 14, 13, 4,
                         13, 99, 3, 1, 1, 9]
    assert output == 1


def test_puzzle_ex_9():

    code_list = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    programme_input = 0
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 0

    code_list = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    programme_input = 3
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 1


def test_puzzle_ex_10():

    code_list = load_computer_data('tests/test_day05_input.txt')
    programme_input = 3
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 999

    code_list = load_computer_data('tests/test_day05_input.txt')
    programme_input = 8
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 1000

    code_list = load_computer_data('tests/test_day05_input.txt')
    programme_input = 13
    code_list, output = run_opcode(code_list, programme_input=programme_input)
    assert output == 1001


def test_puzzle_ex_day2_0():
    code_list, output = run_opcode([1, 0, 0, 0, 99], programme_input=1)
    assert code_list == [2, 0, 0, 0, 99], (
           "Should be 2,0,0,0,99")
    assert output is None


def test_puzzle_ex_day2_1():
    code_list, output = run_opcode([2, 3, 0, 3, 99], programme_input=1)
    assert code_list == [2, 3, 0, 6, 99], (
           "Should be 2,3,0,6,99")
    assert output is None


def test_puzzle_ex_day2_2():
    code_list, output = run_opcode([2, 4, 4, 5, 99, 0], programme_input=1)
    assert code_list == [2, 4, 4, 5, 99, 9801], (
           "Should be 2,4,4,5,99,9801")
    assert output is None


def test_puzzle_ex_day2_3():
    code_list, output = run_opcode([1, 1, 1, 4, 99, 5, 6, 0, 99],
                                   programme_input=1)
    assert code_list == [30, 1, 1, 4, 2, 5, 6, 0, 99], (
           "Should be 30,1,1,4,2,5,6,0,99")
    assert output is None


def test_parse_opcode():
    # Example: 1002
    opcode, parameter_mode_dict = parse_opcode(1002)
    assert opcode == '02'
    assert parameter_mode_dict == {1: '0', 2: '1', 3: '0'}

    # Example: 1101
    opcode, parameter_mode_dict = parse_opcode(1101)
    assert opcode == '01'
    assert parameter_mode_dict == {1: '1', 2: '1', 3: '0'}

    # Example: 99
    opcode, parameter_mode_dict = parse_opcode(99)
    assert opcode == '99'
    assert parameter_mode_dict == {1: '0', 2: '0', 3: '0'}

    # Example: 3
    opcode, parameter_mode_dict = parse_opcode(3)
    assert opcode == '03'
    assert parameter_mode_dict == {1: '0', 2: '0', 3: '0'}

    # Example: 4
    opcode, parameter_mode_dict = parse_opcode(4)
    assert opcode == '04'
    assert parameter_mode_dict == {1: '0', 2: '0', 3: '0'}

    # Example: 1105
    opcode, parameter_mode_dict = parse_opcode(1105)
    assert opcode == '05'
    assert parameter_mode_dict == {1: '1', 2: '1', 3: '0'}

    # Example: 1006
    opcode, parameter_mode_dict = parse_opcode(1006)
    assert opcode == '06'
    assert parameter_mode_dict == {1: '0', 2: '1', 3: '0'}

    # Example: 7
    opcode, parameter_mode_dict = parse_opcode(7)
    assert opcode == '07'
    assert parameter_mode_dict == {1: '0', 2: '0', 3: '0'}

    # Example: 1008
    opcode, parameter_mode_dict = parse_opcode(1008)
    assert opcode == '08'
    assert parameter_mode_dict == {1: '0', 2: '1', 3: '0'}


def test_apply_opcode1():

    code_list = [1101, 100, -1, 4, 0]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list = apply_opcode1(code_list,
                              opcode_loc,
                              parameter_mode_dict)

    assert opcode == '01'
    assert code_list == [1101, 100, -1, 4, 99]


def test_apply_opcode1_exception():

    code_list = [11101, 4, 3, 4, 33]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    with pytest.raises(ForbiddenValueError):
        code_list = apply_opcode1(code_list,
                                  opcode_loc,
                                  parameter_mode_dict)


def test_apply_opcode2():

    code_list = [1002, 4, 3, 4, 33]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list = apply_opcode2(code_list,
                              opcode_loc,
                              parameter_mode_dict)

    assert opcode == '02'
    assert code_list == [1002, 4, 3, 4, 99]


def test_apply_opcode2_exception():

    code_list = [11002, 4, 3, 4, 33]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    with pytest.raises(ForbiddenValueError):
        code_list = apply_opcode2(code_list,
                                  opcode_loc,
                                  parameter_mode_dict)


def test_apply_opcode3():

    code_list = [3, 0, 99]
    opcode_loc = 0
    programme_input = 7

    # Get the opcode and parameter_mode_dict
    code_list = apply_opcode3(code_list,
                              opcode_loc,
                              programme_input=programme_input)

    assert code_list == [7, 0, 99]


def test_apply_opcode4_position():

    code_list = [4, 0, 99]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, output = apply_opcode4(code_list,
                                      opcode_loc,
                                      parameter_mode_dict)

    assert opcode == '04'
    assert code_list == [4, 0, 99]
    assert output == 4


def test_apply_opcode4_immediate():

    code_list = [104, 0, 99]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, output = apply_opcode4(code_list,
                                      opcode_loc,
                                      parameter_mode_dict)

    assert opcode == '04'
    assert code_list == [104, 0, 99]
    assert output == 0


def test_apply_opcode5_position():

    code_list = [5, 1, 3, 3, 99]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, inc_steps = apply_opcode5(code_list,
                                         opcode_loc,
                                         parameter_mode_dict)

    assert opcode == '05'
    assert code_list == [5, 1, 3, 3, 99]
    assert inc_steps == 3


def test_apply_opcode5_immediate():

    code_list = [1005, 3, 5, 2, 1, 4, 2, 99]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, inc_steps = apply_opcode5(code_list,
                                         opcode_loc,
                                         parameter_mode_dict)

    assert opcode == '05'
    assert code_list == [1005, 3, 5, 2, 1, 4, 2, 99]
    assert inc_steps == 5


def test_apply_opcode6_position():

    code_list = [6, 2, 0, 99, 1, 2, 4]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, inc_steps = apply_opcode6(code_list,
                                         opcode_loc,
                                         parameter_mode_dict)

    assert opcode == '06'
    assert code_list == [6, 2, 0, 99, 1, 2, 4]
    assert inc_steps == 6


def test_apply_opcode6_immediate():

    code_list = [1106, 0, 2, 2, 1, 4, 2, 99]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, inc_steps = apply_opcode6(code_list,
                                         opcode_loc,
                                         parameter_mode_dict)

    assert opcode == '06'
    assert code_list == [1106, 0, 2, 2, 1, 4, 2, 99]
    assert inc_steps == 2


def test_apply_opcode7_position():

    code_list = [7, 3, 2, 4, 1]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, inc_steps = apply_opcode7(code_list,
                                         opcode_loc,
                                         parameter_mode_dict)

    assert opcode == '07'
    assert code_list == [7, 3, 2, 4, 0]
    assert inc_steps == 4


def test_apply_opcode7_immediate():

    code_list = [1107, -1, 8, 3, 4]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, inc_steps = apply_opcode7(code_list,
                                         opcode_loc,
                                         parameter_mode_dict)

    assert opcode == '07'
    assert code_list == [1107, -1, 8, 1, 4]
    assert inc_steps == 4


def test_apply_opcode8_position():

    code_list = [8, 4, 4, 2, 0]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, inc_steps = apply_opcode8(code_list,
                                         opcode_loc,
                                         parameter_mode_dict)

    assert opcode == '08'
    assert code_list == [8, 4, 1, 2, 0]
    assert inc_steps == 4


def test_apply_opcode8_immediate():

    code_list = [1108, -1, 8, 3, 4]
    opcode_loc = 0

    # Get the opcode and parameter_mode_dict
    opcode, parameter_mode_dict = parse_opcode(code_list[opcode_loc])

    code_list, inc_steps = apply_opcode8(code_list,
                                         opcode_loc,
                                         parameter_mode_dict)

    assert opcode == '08'
    assert code_list == [1108, -1, 8, 0, 4]
    assert inc_steps == 4


def test_load_computer_data():

    code_list = load_computer_data('day05/input.txt')

    assert len(code_list) == 678
    assert code_list[0] == 3
    assert code_list[-1] == 226


def test_integration():
    """I know the correct answer, lets check that the code gives me it!
    """
    code_list = load_computer_data('day05/input.txt')
    code_list, output = run_opcode(code_list, programme_input=5)
    assert output == 7161591
