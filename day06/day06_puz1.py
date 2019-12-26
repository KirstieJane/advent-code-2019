#! /usr/bin/env python


def load_orbit_data(fname):
    """Read in input file with the orbit information provided.

    Parameters
    ----------
    fname : string
        File provided by advent of code competition
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

    # Loop over the objects in the orbit_dict

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
        orig_obj = str(obj_sun)
        while orbit_dict.get(obj_sun) is not None:
            obj_sun = orbit_dict.get(obj_sun)
            n_orbits += 1
        n_orbit_dict[orig_obj] = (1, n_orbits-1)

    return n_orbit_dict


def calc_tot_orbits(n_orbit_dict):

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
