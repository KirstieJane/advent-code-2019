#! /usr/bin/env python

import numpy as np
import pandas as pd


def module_fuel_req(mass):
    """Calculate the amount of fuel required for a module of a given mass

    Parameters
    ----------
    mass : float
        The mass of the space ship module
    """
    fuel = np.floor(mass / 3.0) - 2.0

    return fuel


def load_module_data(fname):
    """Read in input file with masses for the 50 space ship modules.
    Return pandas dataframe.

    Parameters
    ----------
    fname : string
        File provided by advent of code competition
    """
    df = pd.read_csv(fname, names=['mass'])
    return df


def calc_fuel(df):
    """Calculate the amount of fuel each module requires

    Parameters
    ----------
    df : pandas dataframe
        pandas dataframe containing column named 'mass'

    Returns
    -------
    pandas dataframe
        pandas dataframe containing columns named 'mass' and 'fuel'
    """
    df['fuel'] = module_fuel_req(df['mass'])
    return df


def sum_fuel(df):
    """Add up the values in the 'fuel' column of the data frame

    Parameters
    ----------
    df : pandas dataframe
        pandas dataframe containing columns named 'mass' and 'fuel

    Returns
    -------
    float
        total fuel required as calculated by summing the 'fuel' column
        in the dataframe
    """
    total_fuel = df['fuel'].sum()
    return total_fuel


if __name__ == "__main__":
    """Load in the data, calculate how much fuel each module needs, and then
    add it up and print the total value to the screen.
    """
    df = load_module_data('day01/input.txt')
    df = calc_fuel(df)
    total_fuel = sum_fuel(df)

    print('\n---- Day 1, Puzzle 1 ----')
    print(f'Total fuel: {total_fuel:.0f}')
