from day02.day02_puz1 import run_opcode, load_computer_data, adjust_data


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


def test_integration():
    """I know the correct answer, lets check that the code gives me it!
    """
    code_list = load_computer_data('day02/input.txt')
    code_list = adjust_data(code_list)
    code_list = run_opcode(code_list)
    assert code_list[0] == 7594646
