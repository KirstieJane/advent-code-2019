from day01.day01_puz1 import (module_fuel_req, load_module_data,
                              calc_fuel, sum_fuel)
from pandas.util.testing import assert_frame_equal, assert_series_equal
import pandas as pd


def test_puzzle_ex_12():
    assert module_fuel_req(12) == 2, "Should be 2"


def test_puzzle_ex_14():
    assert module_fuel_req(14) == 2, "Should be 2"


def test_puzzle_ex_1969():
    assert module_fuel_req(1969) == 654, "Should be 654"


def test_puzzle_ex_100756():
    assert module_fuel_req(100756) == 33583, "Should be 33583"


def create_test_data():
    test_df = pd.DataFrame({'mass': [12, 14, 1969, 100756],
                            'fuel': [2, 2, 654, 33583]}, dtype='float')
    return test_df


def test_load_module_data():
    df_fix = pd.read_csv('day01/input.txt', names=['mass'])
    df = load_module_data('day01/input.txt')
    assert_frame_equal(df_fix, df)
    assert df.shape == (100, 1), "Should be 100 rows and 1 column"


def test_calc_fuel():
    df = load_module_data('day01/input.txt')
    df = calc_fuel(df)
    assert df.shape == (100, 2), "Should be 100 rows and 2 columns"
    assert list(df.columns) == ['mass', 'fuel']
    test_df = create_test_data()
    test_df['fuel_calc'] = test_df['fuel']
    calc_fuel(test_df)
    assert_series_equal(test_df['fuel'], test_df['fuel_calc'],
                        check_names=False)


def test_sum_fuel():
    test_df = create_test_data()
    assert sum_fuel(test_df) == 34241, "Should be 34241"


def test_integration():
    """I know the correct answer, lets check that the code gives me it!
    """
    df = load_module_data('day01/input.txt')
    df = calc_fuel(df)
    total_fuel = sum_fuel(df)
    assert total_fuel == 3406432
