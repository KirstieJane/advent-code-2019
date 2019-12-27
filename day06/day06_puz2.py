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


def build_orbit_graph(orbit_dict):
    """Convert the orbit_dict - a directed network - into orbit_graph - an
    undirected network.

    Parameters
    ----------
    orbit_dict : dictionary
        A dictionary where the keys are the moon objects in teh

    Returns
    -------
    orbit_graph : dictionary
        A dictionary where the keys are every object in the map and the values
        are a list of objects that each object is connected to (either
        orbiting or being orbited by).
    """

    # Create an empty graph
    orbit_graph = {}

    # Loop through all the keys and object in orbit_dict and add them to the
    # orbit_graph
    for obj_sun, obj_moon in orbit_dict.items():
        orbit_graph.setdefault(obj_sun, []).append(obj_moon)
        orbit_graph.setdefault(obj_moon, []).append(obj_sun)

    # Sort the lists so they're easier to test
    for key, value in orbit_graph.items():
        orbit_graph[key] = sorted(value)

    return orbit_graph


def find_shortest_path(orbit_graph, obj_start, obj_end, path=[]):
    """Find the shortest path between the start and end objects in a graph

    This code is copied from the Python Patterns - Implementing Graphs essay at
    https://www.python.org/doc/essays/graphs. It is gratefully re-used under
    the PSF license.

    Parameters
    ----------
    orbit_graph : dict
        A dictionary containing every planet (object) as keys, and the list of
        objects that they connect to (either orbiting or being orbited by)
        for the values.
    obj_start : str
        The name of the starting object
    obj_end : str
        The name of the end object
    path : list
        Objects that must be traversed in the path from obj_start to obj_end,
        Default: []

    Returns
    -------
    shortest : list
        The shortest path between two objects. This path contains both the
        start and end objects.
    """
    path = path + [obj_start]

    # If the start object is the same as the end object then return the path
    # right at the start! It will be 1 element long.
    if obj_start == obj_end:
        return path

    # If the start object is not in the graph then return None
    if obj_start not in orbit_graph:
        return None

    # We're going to find the shortest path here, start by calling it None
    shortest = None

    # Step through the nodes from the start object
    for node in orbit_graph[obj_start]:

        # If the node is not in the path then call **this same function** to
        # find the shortest path between that object and the end object!
        # pass the path we've created to that function.
        if node not in path:
            newpath = find_shortest_path(orbit_graph, node, obj_end, path)

            # If we find a new path compare it to the length of the shortest
            # path. If it is shorter then replace "shortest" with this new path
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest


if __name__ == "__main__":
    """Load in the data, adjust it to the state before the computer caught fire,
    then run the opcode and print the value in position 0 to the screen.
    """
    orbit_dict = load_orbit_data('day06/input.txt')

    print('\n---- Day 6, Puzzle 2 ----')
    orbit_graph = build_orbit_graph(orbit_dict)
    shortest_path = find_shortest_path(orbit_graph, 'YOU', 'SAN')
    min_orbital_transfers = len(shortest_path) - 3

    print(f'Minimum orbital transfers required: {min_orbital_transfers}')
