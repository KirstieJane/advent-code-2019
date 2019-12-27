from day06.day06_puz2 import (load_orbit_data, build_orbit_graph,
                              find_shortest_path)
import pytest


@pytest.mark.parametrize('input_file',
                         ['tests/test_day06_input2.txt',
                          'tests/test_day06_input2_shuffled.txt'])
def test_puzzle_ex_0(input_file):

    test_orbit_dict = load_orbit_data(input_file)
    test_orbit_graph = build_orbit_graph(test_orbit_dict)
    shortest_path = find_shortest_path(test_orbit_graph, 'YOU', 'SAN')
    min_orbital_transfers = len(shortest_path) - 3
    assert min_orbital_transfers == 4


@pytest.mark.parametrize('input_file',
                         ['tests/test_day06_input2.txt',
                          'tests/test_day06_input2_shuffled.txt'])
def test_load_orbit_data(input_file):

    test_orbit_dict = load_orbit_data(input_file)

    assert sorted(set(test_orbit_dict.keys())) == ['B', 'C', 'D', 'E', 'F',
                                                   'G', 'H', 'I', 'J', 'K',
                                                   'L', 'SAN', 'YOU']
    assert sorted(set(test_orbit_dict.values())) == ['B', 'C', 'COM', 'D', 'E',
                                                     'G', 'I', 'J', 'K']
    assert len(test_orbit_dict) == 13

    orbit_dict = load_orbit_data('day06/input.txt')

    assert orbit_dict['12Q'] == 'YMK'  # Test the first entry in the data
    assert orbit_dict['N9V'] == 'KXX'  # Test the last entry in the data
    assert len(orbit_dict) == 1713


@pytest.mark.parametrize('input_file',
                         ['tests/test_day06_input2.txt',
                          'tests/test_day06_input2_shuffled.txt'])
def test_build_orbit_graph(input_file):

    test_orbit_dict = load_orbit_data(input_file)

    test_orbit_graph = build_orbit_graph(test_orbit_dict)

    assert sorted(test_orbit_graph.keys()) == ['B', 'C', 'COM', 'D', 'E', 'F',
                                               'G', 'H', 'I', 'J', 'K', 'L',
                                               'SAN', 'YOU']

    assert sorted(test_orbit_graph.values()) == [['B'], ['B', 'D'], ['B', 'H'],
                                                 ['C', 'COM', 'G'],
                                                 ['C', 'E', 'I'],
                                                 ['D', 'F', 'J'], ['D', 'SAN'],
                                                 ['E'], ['E', 'K'], ['G'],
                                                 ['I'], ['J', 'L', 'YOU'],
                                                 ['K'], ['K']]


@pytest.mark.parametrize('input_file',
                         ['tests/test_day06_input2.txt',
                          'tests/test_day06_input2_shuffled.txt'])
def test_find_shortest_path(input_file):

    test_orbit_dict = load_orbit_data(input_file)
    test_orbit_graph = build_orbit_graph(test_orbit_dict)

    shortest_path = find_shortest_path(test_orbit_graph, 'YOU', 'SAN')
    assert shortest_path == ['YOU', 'K', 'J', 'E', 'D', 'I', 'SAN']

    shortest_path = find_shortest_path(test_orbit_graph, 'J', 'H')
    assert shortest_path == ['J', 'E', 'D', 'C', 'B', 'G', 'H']

    # Test that if the object isn't in the graph then the shortest path is None
    shortest_path = find_shortest_path(test_orbit_graph, 'Q', 'H')
    assert shortest_path is None

    # Test that if the start adn end objects are the same then the shortest
    # path is just a list of the single object
    shortest_path = find_shortest_path(test_orbit_graph, 'H', 'H')
    assert shortest_path == ['H']


def test_integration():
    """I know the correct answer, lets check that the code gives me it!
    """
    orbit_dict = load_orbit_data('day06/input.txt')
    orbit_graph = build_orbit_graph(orbit_dict)
    shortest_path = find_shortest_path(orbit_graph, 'YOU', 'SAN')
    min_orbital_transfers = len(shortest_path) - 3

    assert min_orbital_transfers == 517
