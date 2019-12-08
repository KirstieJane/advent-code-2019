#! /usr/bin/env python

import numpy as np
import pandas as pd


def module_fuel_req(mass):
    """Calculate the amount of fuel required for a module of a given mass
    taking into account the additional fuel that is required for the required
    fuel itself!

    Parameters
    ----------
    mass : float
        The mass of the space ship module
    """
    total_fuel = 0

    # Calculate the amount of fuel needed for the space ship module
    fuel = mass_fuel_req(mass)

    # Add to the total fuel value
    total_fuel += fuel

    # Iteratively calculate the additional fuel needed due to the weight
    # of the fuel itself and add to the total fuel amount
    while fuel > 0:
        fuel = mass_fuel_req(fuel)
        total_fuel += fuel

    return total_fuel


def mass_fuel_req(mass):
    """Calculate the amount of fuel required for a given mass

    Parameters
    ----------
    mass : float
        the mass of the item (module of the space ship, or fuel for example)
    """
    fuel = np.floor(mass / 3.0) - 2.0

    fuel = fuel if fuel > 0 else 0

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
    df['fuel'] = df['mass'].apply(module_fuel_req)
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

    print('\n---- Day 1, Puzzle 2 ----')
    print(f'Total fuel: {total_fuel:.0f}')
