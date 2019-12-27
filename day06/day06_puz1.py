#! /usr/bin/env python


def load_orbit_data(fname):
    """Read in input file with the orbit information provided.

    Parameters
    ----------
    fname : string
        File provided by advent of code competition

    Returns
    -------
    orbit_dict : dictionary
        A dictionary where each key is a moon object in the system, and the
        value is the sun object (the thing it orbits).
    """
    # Create empty orbit dictionary
    orbit_dict = {}

    # Read in each line, and split by comma
    with open(fname, 'r') as f:
        for line in f:
            obj_sun, obj_moon = [obj.strip() for obj in line.split(')')]
            orbit_dict[obj_moon] = obj_sun

    return orbit_dict


def build_n_orbit_dict(orbit_dict):
    """[summary]

    Parameters
    ----------
    orbit_dict : dictionary
        A dictionary where each key is a moon object in the system, and the
        value is the sun object (the thing it orbits).

    Returns
    -------
    n_orbit_dict : dictionary
        A dictionary where each key is an object in the system and each value
        is a tuple of 2 values. The first represents the number of direct
        orbits and the second the number of indirect orbits.
    """
    # Start with an empty n_orbit_dict
    n_orbit_dict = {}

    # Start at the center of mass of the universe. This does not appear in the
    # keys of the orbit_dict because it doesn't orbit anything.
    # COM has 0 direct and 0 indirect orbits for a total of 0 orbits.
    obj_sun = 'COM'
    n_orbit_dict[obj_sun] = (0, 0)

    # Now loop through all the other objects. Replace the original sun object
    # with all the others before it in order to calculate the number of
    # indirect orbits.
    for obj_sun in orbit_dict.keys():
        n_orbits = 0
        # Save the original obj_sun so we can write this as the
        # key of n_orbit_dict
        orig_obj = str(obj_sun)

        # Keep getting the object that this object orbits until the objec
        # isn't in the dictionary and returns None. Increase the number of
        # orbits each time.
        while orbit_dict.get(obj_sun) is not None:
            obj_sun = orbit_dict.get(obj_sun)
            n_orbits += 1
        n_orbit_dict[orig_obj] = (1, n_orbits-1)

    return n_orbit_dict


def calc_tot_orbits(n_orbit_dict):
    """Calculate the total number of direct and indirect orbits in
    n_orbit_dict.

    Parameters
    ----------
    n_orbit_dict : dictionary
        A dictionary where each key is an object in the system and each value
        is a tuple of 2 values. The first represents the number of direct
        orbits and the second the number of indirect orbits.

    Returns
    -------
    n_direct_tot : int
        The number of direct orbits
    n_indirect_tot : int
        The number of indirect orbits
    """

    n_direct_tot = sum([n_orbits[0] for n_orbits in n_orbit_dict.values()])
    n_indirect_tot = sum([n_orbits[1] for n_orbits in n_orbit_dict.values()])

    return n_direct_tot, n_indirect_tot


if __name__ == "__main__":
    """Load in the data, adjust it to the state before the computer caught fire,
    then run the opcode and print the value in position 0 to the screen.
    """
    orbit_dict = load_orbit_data('day06/input.txt')

    print('\n---- Day 6, Puzzle 1 ----')
    n_orbit_dict = build_n_orbit_dict(orbit_dict)
    n_direct_tot, n_indirect_tot = calc_tot_orbits(n_orbit_dict)
    print(f'Total direct orbits: {n_direct_tot}')
    print(f'Total indirect orbits: {n_indirect_tot}')
    print(f'Total orbits: {n_direct_tot + n_indirect_tot}')
