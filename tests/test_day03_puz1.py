from day03.day03_puz1 import (find_min_manhatten_dist, wire_path_str_to_list,
                              steps_to_coords, path_list_to_set,
                              manhatten_dist_from_str, load_input_data)
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
    test_data0_set_wire0 = set(((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                                (6, 0), (7, 0), (8, 0),
                                (8, 1), (8, 2), (8, 3), (8, 4), (8, 5),
                                (7, 5), (6, 5), (5, 5), (4, 5), (3, 5),
                                (3, 4), (3, 3), (3, 2)))
    test_data0_set_wire1 = set(((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                                (0, 6), (0, 7),
                                (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7),
                                (6, 6), (6, 5), (6, 4), (6, 3),
                                (5, 3), (4, 3), (3, 3), (2, 3)))
    test_data1 = ('R75,D30,R83,U83,L12,D49,R71,U7,L72',
                  'U62,R66,U55,R34,D71,R55,D58,R83')
    test_data2 = ('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51',
                  'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7')

    test_data_dict = {'test_data0': test_data0,
                      'test_data0_list': test_data0_list,
                      'test_data0_set_wire0': test_data0_set_wire0,
                      'test_data0_set_wire1': test_data0_set_wire1,
                      'test_data1': test_data1,
                      'test_data2': test_data2}

    return test_data_dict


def test_puzzle_ex_0(define_test_data):
    test_data0 = define_test_data['test_data0']
    (closest_crossover,
     manhatten_dist) = manhatten_dist_from_str(test_data0)
    assert manhatten_dist == 6, "Should be 6"


def test_puzzle_ex_1(define_test_data):
    test_data1 = define_test_data['test_data1']
    (closest_crossover,
     manhatten_dist) = manhatten_dist_from_str(test_data1)
    assert manhatten_dist == 159, "Should be 159"


def test_puzzle_ex_2(define_test_data):
    test_data2 = define_test_data['test_data2']
    (closest_crossover,
     manhatten_dist) = manhatten_dist_from_str(test_data2)
    assert manhatten_dist == 135, "Should be 135"


def test_load_input_data():
    instruction_tuple = load_input_data('day03/input.txt')
    assert len(instruction_tuple[0]) == 1473
    assert len(instruction_tuple[1]) == 1467


def test_wire_path_str_to_list(define_test_data):
    test_data0 = define_test_data['test_data0']
    test_data0_list = define_test_data['test_data0_list']
    assert wire_path_str_to_list(test_data0[0]) == test_data0_list[0]
    assert wire_path_str_to_list(test_data0[1]) == test_data0_list[1]


def test_path_list_to_set(define_test_data):
    test_data0_list = define_test_data['test_data0_list']
    test_data0_list_wire0 = test_data0_list[0]
    test_data0_list_wire1 = test_data0_list[1]
    test_data0_set_wire0 = define_test_data['test_data0_set_wire0']
    test_data0_set_wire1 = define_test_data['test_data0_set_wire1']

    coords_wire0 = path_list_to_set(test_data0_list_wire0)
    coords_wire1 = path_list_to_set(test_data0_list_wire1)

    assert coords_wire0 == test_data0_set_wire0
    assert coords_wire1 == test_data0_set_wire1


def test_steps_to_coords():
    """Give an instruction of going 3 steps to the right (3, 0)
    starting from point (4, 9) and check that the end point is (7, 9)
    and the wire coordinates set has the right entries
    """
    wire_coords = set()
    wire_coords.add((4, 9))

    ((start_x, start_y),
     wire_coords) = steps_to_coords(3, 0,
                                    4, 9,
                                    wire_coords)
    assert start_x == 7
    assert start_y == 9
    assert wire_coords == set(((4, 9), (5, 9), (6, 9), (7, 9)))


def test_find_min_manhatten_dist(define_test_data):
    test_data0_set_wire0 = define_test_data['test_data0_set_wire0']
    test_data0_set_wire1 = define_test_data['test_data0_set_wire1']

    (closest_crossover,
     manhatten_dist) = find_min_manhatten_dist(test_data0_set_wire0,
                                               test_data0_set_wire1)

    assert closest_crossover == (3, 3)
    assert manhatten_dist == 6


def test_integration():
    """I know the correct answer, lets check that the code gives me it!
    """
    instruction_tuple = load_input_data('day03/input.txt')
    (closest_crossover,
     manhatten_dist) = manhatten_dist_from_str(instruction_tuple)
    assert closest_crossover == (-1028, 2201)
    assert manhatten_dist == 3229
