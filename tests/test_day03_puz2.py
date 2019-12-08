from day03.day03_puz2 import (find_fewest_steps_crosspoint,
                              wire_path_str_to_list, load_input_data,
                              steps_to_coords, path_list_to_dict,
                              get_fewest_steps_to_intersec)
import pytest


@pytest.fixture
def define_test_data():
    """Read in the example data from the puzzle description

    Returns
    -------
    test_data0: tuple
        A tuple of two strings containing the wire instructions for the worked
        example
    test_data1_list : list
        A list containing pairs of x, y coordinates that define a path from
        the previous point
    test_data0_dict_wire1: dict
        A dictionary containing all the x, y coorindates that the first wire
        in example 0 passes through and the number of steps taken to get there
    test_data0_dict_wire1: dict
        A dictionary containing all the x, y coorindates that the second wire
        in example 0 passes through and the number of steps taken to get there
    test_data1 : tuple
        A tuple of two strings containing the wire instructions for the first
        additional example
    test_data2 : tuple
        A tuple of two strings containing the wire instructions for the second
        additional example
    """
    test_data0 = ('R8,U5,L5,D3', 'U7,R6,D4,L4')
    test_data0_list = ([(8, 0), (0, 5), (-5, 0), (0, -3)],
                       [(0, 7), (6, 0), (0, -4), (-4, 0)])
    test_data0_dict_wire0 = {(0, 0): [0], (1, 0): [1], (2, 0): [2],
                             (3, 0): [3], (4, 0): [4], (5, 0): [5],
                             (6, 0): [6], (7, 0): [7], (8, 0): [8],
                             (8, 1): [9], (8, 2): [10], (8, 3): [11],
                             (8, 4): [12], (8, 5): [13],
                             (7, 5): [14], (6, 5): [15], (5, 5): [16],
                             (4, 5): [17], (3, 5): [18],
                             (3, 4): [19], (3, 3): [20], (3, 2): [21]}
    test_data0_dict_wire1 = {(0, 0): [0], (0, 1): [1], (0, 2): [2],
                             (0, 3): [3], (0, 4): [4], (0, 5): [5],
                             (0, 6): [6], (0, 7): [7],
                             (1, 7): [8], (2, 7): [9], (3, 7): [10],
                             (4, 7): [11], (5, 7): [12], (6, 7): [13],
                             (6, 6): [14], (6, 5): [15], (6, 4): [16],
                             (6, 3): [17],
                             (5, 3): [18], (4, 3): [19], (3, 3): [20],
                             (2, 3): [21]}
    test_data1 = ('R75,D30,R83,U83,L12,D49,R71,U7,L72',
                  'U62,R66,U55,R34,D71,R55,D58,R83')
    test_data2 = ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                  'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')

    test_data_dict = {'test_data0': test_data0,
                      'test_data0_list': test_data0_list,
                      'test_data0_dict_wire0': test_data0_dict_wire0,
                      'test_data0_dict_wire1': test_data0_dict_wire1,
                      'test_data1': test_data1,
                      'test_data2': test_data2}

    return test_data_dict


def test_puzzle_ex_0(define_test_data):
    test_data0 = define_test_data['test_data0']
    (fewest_crossover,
     fewest_steps0,
     fewest_steps1) = get_fewest_steps_to_intersec(test_data0)
    assert fewest_steps0 == 15, "Should be 15"
    assert fewest_steps1 == 15, "Should be 15"
    fewest_steps_tot = fewest_steps0 + fewest_steps1
    assert fewest_steps_tot == 30, "Should be 30"


def test_puzzle_ex_1(define_test_data):
    test_data1 = define_test_data['test_data1']
    (fewest_crossover,
     fewest_steps0,
     fewest_steps1) = get_fewest_steps_to_intersec(test_data1)
    fewest_steps_tot = fewest_steps0 + fewest_steps1
    assert fewest_steps_tot == 610, "Should be 610"


def test_puzzle_ex_2(define_test_data):
    test_data2 = define_test_data['test_data2']
    (fewest_crossover,
     fewest_steps0,
     fewest_steps1) = get_fewest_steps_to_intersec(test_data2)
    fewest_steps_tot = fewest_steps0 + fewest_steps1
    assert fewest_steps_tot == 410, "Should be 410"


def test_load_input_data():
    instruction_tuple = load_input_data('day03/input.txt')
    assert len(instruction_tuple[0]) == 1473
    assert len(instruction_tuple[1]) == 1467


def test_wire_path_str_to_list(define_test_data):
    test_data0 = define_test_data['test_data0']
    test_data0_list = define_test_data['test_data0_list']
    assert wire_path_str_to_list(test_data0[0]) == test_data0_list[0]
    assert wire_path_str_to_list(test_data0[1]) == test_data0_list[1]


def test_path_list_to_dict(define_test_data):
    test_data0_list = define_test_data['test_data0_list']
    test_data0_list_wire0 = test_data0_list[0]
    test_data0_list_wire1 = test_data0_list[1]
    test_data0_dict_wire0 = define_test_data['test_data0_dict_wire0']
    test_data0_dict_wire1 = define_test_data['test_data0_dict_wire1']

    coords_wire0 = path_list_to_dict(test_data0_list_wire0)
    coords_wire1 = path_list_to_dict(test_data0_list_wire1)

    assert coords_wire0 == test_data0_dict_wire0
    assert coords_wire1 == test_data0_dict_wire1


def test_steps_to_coords_allnew():
    """Give an instruction of going 3 steps to the right (3, 0)
    starting from point (4, 9) which is 23 steps into the whole wire's path
    and check that the end point is (7, 9), the updated total steps is 26 and
    the wire coordinates set has the right entries.
    """
    wire_coords = dict()
    n_steps = 23
    wire_coords[(4, 9)] = [n_steps]

    ((start_x, start_y),
     wire_coords, n_steps) = steps_to_coords(3, 0,
                                             4, 9,
                                             wire_coords, n_steps)

    assert start_x == 7
    assert start_y == 9
    assert n_steps == 26
    assert wire_coords == {(4, 9): [23],
                           (5, 9): [24],
                           (6, 9): [25],
                           (7, 9): [26]}


def test_steps_to_coords_crossover():
    """Give an instruction of going 4 steps down (0, -4)
    starting from point (0, 2) which is 12 steps into the whole wire's path
    and check that the end point is (0, -2), the updated total steps is 16 and
    the wire coordinates set has the right entries. Specifically, this means
    that the origin should appear twice in the output
    """
    wire_coords = dict()
    wire_coords[(0, 0)] = [0]
    n_steps = 12
    wire_coords[(0, 2)] = [n_steps]

    ((start_x, start_y),
     wire_coords, n_steps) = steps_to_coords(0, -4,
                                             0, 2,
                                             wire_coords, n_steps)

    assert start_x == 0
    assert start_y == -2
    assert n_steps == 16
    assert wire_coords == {(0, 2): [12],
                           (0, 1): [13],
                           (0, 0): [0, 14],
                           (0, -1): [15],
                           (0, -2): [16]}


def test_find_fewest_steps_crosspoint(define_test_data):
    test_data0_dict_wire0 = define_test_data['test_data0_dict_wire0']
    test_data0_dict_wire1 = define_test_data['test_data0_dict_wire1']

    (fewest_crossover,
     fewest_steps0,
     fewest_steps1) = find_fewest_steps_crosspoint(test_data0_dict_wire0,
                                                   test_data0_dict_wire1)

    fewest_steps_tot = fewest_steps0 + fewest_steps1

    assert fewest_crossover == (6, 5)
    assert fewest_steps0 == 15
    assert fewest_steps1 == 15
    assert fewest_steps_tot == 30


def test_integration():
    """I know the correct answer, lets check that the code gives me it!
    """
    instruction_tuple = load_input_data('day03/input.txt')
    (fewest_crossover,
     fewest_steps0,
     fewest_steps1) = get_fewest_steps_to_intersec(instruction_tuple)

    fewest_steps_tot = fewest_steps0 + fewest_steps1

    assert fewest_crossover == (2787, 1921)
    assert fewest_steps_tot == 32132
