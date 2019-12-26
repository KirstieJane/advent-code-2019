from day06.day06_puz1 import (load_orbit_data, build_n_orbit_dict,
                              calc_tot_orbits)
import pytest


@pytest.mark.parametrize('input_file', ['tests/test_day06_input.txt',
                                        'tests/test_day06_input_shuffled.txt'])
def test_puzzle_ex_0(input_file):

    test_orbit_dict = load_orbit_data(input_file)
    n_orbit_dict = build_n_orbit_dict(test_orbit_dict)
    n_direct_tot, n_indirect_tot = calc_tot_orbits(n_orbit_dict)
    assert n_direct_tot == 11
    assert n_indirect_tot == 31


@pytest.mark.parametrize('input_file', ['tests/test_day06_input.txt',
                                        'tests/test_day06_input_shuffled.txt'])
def test_load_orbit_data(input_file):

    test_orbit_dict = load_orbit_data(input_file)

    assert sorted(set(test_orbit_dict.keys())) == sorted(set(['B', 'C', 'D',
                                                              'E', 'F', 'G',
                                                              'H', 'I', 'J',
                                                              'K', 'L']))
    assert sorted(set(test_orbit_dict.values())) == sorted(set(['B', 'C',
                                                                'COM', 'D',
                                                                'E', 'G', 'J',
                                                                'K']))
    assert len(test_orbit_dict) == 11

    orbit_dict = load_orbit_data('day06/input.txt')

    assert orbit_dict['12Q'] == 'YMK'  # Test the first entry in the data
    assert orbit_dict['N9V'] == 'KXX'  # Test the last entry in the data
    assert len(orbit_dict) == 1713


@pytest.mark.parametrize('input_file', ['tests/test_day06_input.txt',
                                        'tests/test_day06_input_shuffled.txt'])
def test_calc_orbits(input_file):

    test_orbit_dict = load_orbit_data(input_file)
    n_orbit_dict = build_n_orbit_dict(test_orbit_dict)

    # 'COM' orbits nothing
    assert n_orbit_dict['COM'] == (0, 0)
    # 'B' orbits 'COM': 1 direct orbit, 0 indirect orbits
    assert n_orbit_dict['B'] == (1, 0)
    # 'C' orbits 'B': 1 direct orbit, 1 indirect orbit
    assert n_orbit_dict['C'] == (1, 1)
    # 'D' orbits 'C': 1 direct orbit, 2 indirect orbits
    assert n_orbit_dict['D'] == (1, 2)
    # 'E' orbits 'D': 1 direct orbit, 3 indirect orbits
    assert n_orbit_dict['E'] == (1, 3)
    # 'F' orbits 'E': 1 direct orbit, 4 indirect orbits
    assert n_orbit_dict['F'] == (1, 4)
    # 'G' orbits 'B': 1 direct orbit, 1 indirect orbit
    assert n_orbit_dict['G'] == (1, 1)
    # 'H' orbits 'G': 1 direct orbit, 2 indirect orbits
    assert n_orbit_dict['H'] == (1, 2)
    # 'I' orbits 'D': 1 direct orbit, 3 indirect orbits
    assert n_orbit_dict['I'] == (1, 3)
    # 'J' orbits 'E': 1 direct orbit, 4 indirect orbits
    assert n_orbit_dict['J'] == (1, 4)
    # 'K' orbits 'J': 1 direct orbit, 5 indirect orbits
    assert n_orbit_dict['K'] == (1, 5)
    # 'L' orbits 'K': 1 direct orbit, 6 indirect orbits
    assert n_orbit_dict['L'] == (1, 6)


# def test_integration():
#     """I know the correct answer, lets check that the code gives me it!
#     """
#     orbit_dict = load_orbit_data('day06/input.txt')
#     n_direct, n_indirect = calc_orbits(orbit_dict)
#     n_total = n_direct + n_indirect
#     assert n_total == 7161591
