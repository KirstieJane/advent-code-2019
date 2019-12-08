#! /usr/bin/env python


def get_fewest_steps_to_intersec(instruction_tuple):

    # Split up the first and second instructions
    instruction_str_wire0, instruction_str_wire1 = instruction_tuple

    # Convert the string instructions to lists containing hor and vert
    # integer tuples
    path_list_wire0 = wire_path_str_to_list(instruction_str_wire0)
    path_list_wire1 = wire_path_str_to_list(instruction_str_wire1)

    # Convert these lists of instructions into sets of coordinates through
    # which the wires pass
    wire_coords_wire0 = path_list_to_dict(path_list_wire0)
    wire_coords_wire1 = path_list_to_dict(path_list_wire1)

    (fewest_steps0,
     fewest_steps1,
     fewest_crossover) = find_fewest_steps_crosspoint(wire_coords_wire0,
                                                      wire_coords_wire1)

    return fewest_steps0, fewest_steps1, fewest_crossover


def load_input_data(input_file):
    """Read in the input file to a tuple of two strings

    Parameters
    ----------
    input_file : filename
        File containing two rows consisting of comma separated strings
        corresponding to instructions to outline the path for two wires

    Returns
    -------
    instruction_tuple : tuple
        tuple of two strings, one corresponding to each wire
    """
    instruction_list = []

    with open(input_file, 'r') as f:
        for line in f:
            instruction_list += [line.strip()]

    instruction_tuple = tuple(instruction_list)

    return instruction_tuple


def wire_path_str_to_list(instruction_str):
    """Split up a string with multiple instuctions that correspond to the path
    that the wire follows to individual horizontal and vertical paths into a
    list containing the individual steps.

    Parameters
    ----------
    instruction_str : str
        comma separated string of multiple instructions that define a wire path

    Returns
    -------
    path_list : list
        a list of x, y coordinates (all integers) where each element in the
        list corresponds to a horizontal or vertical path that the wire follows
        from the previous point
    """
    path_list = []

    for instruction in instruction_str.split(','):

        coords = str_to_coords(instruction)

        path_list += [coords]

    return path_list


def path_list_to_dict(wire_path_list):
    """Convert a set of instructions (as (hor, vert) tuples) into a dictionary
    of coordinates through which the wire moves after starting at origin (0, 0)
    where the values for each coordinate is the number of steps that the wire
    took to get to it

    Parameters
    ----------
    wire_path_list : list
        a list of (hor, vert) values that contain the instructions
        for where the wire goes around the grid

    Returns
    -------
    wire_coords : dict
        keys of dictionary are coordinates through which the wire passes
        values are the number of steps that the wire has taken to get to that
        point (list)
    """
    # Start at 0
    origin = (0, 0)
    start_x, start_y = origin
    n_steps = 0

    # Create an empty dictionary to hold all the coordinates that the wire
    # passes through and the number of steps it takes to get there
    # and then add the origin
    wire_coords = dict()
    wire_coords[origin] = [0]

    # Go through all the steps in the wire_path_list and turn those steps into
    # coordinates saved in the wire_coords set
    for hor_steps, vert_steps in wire_path_list:
        ((start_x, start_y),
         wire_coords, n_steps) = steps_to_coords(hor_steps, vert_steps,
                                                 start_x, start_y,
                                                 wire_coords, n_steps)

    return wire_coords


def steps_to_coords(hor_steps, vert_steps,
                    start_x, start_y,
                    wire_coords, n_steps):
    """Add coordinates to a set of points that the wire passes through. They
    are defined as a number of steps horizontally or vertically from the
    starting point for this particular instruction.

    Parameters
    ----------
    hor_steps : int
        number of steps to take along the x direction
    vert_steps : int
        number of steps to take along the y direction
    start_x : int
        x coordinate of starting point
    start_y : int
        y coordinate of starting point
    wire_coords : dict
        keys of dictionary are coordinates through which the wire passes
        values are the number of steps that the wire has taken to get to that
        point (list)
    n_steps: int
        number of steps that the wire has taken so far

    Returns
    -------
    start_x : int
        x coordinate of end point
        (will be the starting point for the next instruction)
    start_y : int
        y coordinate of end point
        (will be the starting point for the next instruction)
    wire_coords : dict
        keys of dictionary are coordinates through which the wire passes
        values are the number of steps that the wire has taken to get to that
        point (list)
    n_steps : int
        total number of steps taken to the end point
        (will be the starting point for the next iteration)
    """
    if hor_steps > 0:
        for x in range(1, hor_steps + 1):
            if (start_x + x, start_y) in wire_coords.keys():
                wire_coords[(start_x + x, start_y)] += [n_steps + x]
            else:
                wire_coords[(start_x + x, start_y)] = [n_steps + x]
    elif hor_steps < 0:
        for x in range(1, (-1) * hor_steps + 1):
            if (start_x - x, start_y) in wire_coords.keys():
                wire_coords[(start_x - x, start_y)] += [n_steps + x]
            else:
                wire_coords[(start_x - x, start_y)] = [n_steps + x]

    if vert_steps > 0:
        for y in range(1, vert_steps + 1):
            if (start_x, start_y + y) in wire_coords.keys():
                wire_coords[(start_x, start_y + y)] += [n_steps + y]
            else:
                wire_coords[(start_x, start_y + y)] = [n_steps + y]
    elif vert_steps < 0:
        for y in range(1, (-1) * vert_steps + 1):
            if (start_x, start_y - y) in wire_coords.keys():
                wire_coords[(start_x, start_y - y)] += [n_steps + y]
            else:
                wire_coords[(start_x, start_y - y)] = [n_steps + y]

    start_x, start_y = start_x + hor_steps, start_y + vert_steps

    n_steps = n_steps + abs(hor_steps) + abs(vert_steps)

    return (start_x, start_y), wire_coords, n_steps


def str_to_coords(instruction):
    """Split an instruction (eg R10 or L4 etc) into a direction and the number
    of steps to take and convert that into an x, y pair of coordinates that
    define the number of steps from the start point for that instruction

    Parameters
    ----------
    instruction : str
        A line segment from the wire.
        For example R10 which corresponds to taking 10 steps to the right from
        the starting point.

    Returns
    -------
    coords
        A pair of x, y coordinates corresponding to the instruction
    """
    # Split the instruction into an initial direction (R, L, U or D) and
    # distance (the number of steps in that direction)
    direction, steps = instruction[0], int(instruction[1:])

    # Format the coordinates according to the direction
    if direction == 'R':
        coords = (steps, 0)
    elif direction == 'U':
        coords = (0, steps)
    elif direction == 'L':
        coords = (-1*steps, 0)
    elif direction == 'D':
        coords = (0, -1*steps)

    return coords


def find_fewest_steps_crosspoint(wire_coords0, wire_coords1):
    """Find all the points where two wires cross and calculate the number of
    steps taken to get to each of them. Return the coordinate that takes
    the fewest steps in total.

    Parameters
    ----------
    wire_coords0 : dict
        coordinates that the first wire passes through
    wire_coords1 : dict
        coordinates that the second wire passes through

    Returns
    -------
    fewest_crossover : tuple
        coordinates of cross over point that requires fewest total steps
    fewest_steps0 : int
        number of steps that are needed to be taken by the first wire to get
        to the fewest_crossover point
    fewest_steps1 : int
        number of steps that are needed to be taken by the second wire to get
        to the fewest_crossover point
    """
    n_steps_dict = {}
    for x, y in set(wire_coords0).intersection(set(wire_coords1)):
        if not (x, y) == (0, 0):
            # Add an entry to the n_steps_dict for the coordinate
            # which is the sum of the minimum number of steps needed to get to
            # that point for the first wire, and the minimum number of steps
            # needed to get there for the second wire
            n_steps_dict[(x, y)] = (min(wire_coords0[(x, y)]) +
                                    min(wire_coords1[(x, y)]))

    # Get the point where the wires cross that has the total number of steps
    fewest_crossover = min(n_steps_dict, key=n_steps_dict.get)
    fewest_steps0 = wire_coords0[fewest_crossover][0]
    fewest_steps1 = wire_coords1[fewest_crossover][0]

    return fewest_crossover, fewest_steps0, fewest_steps1


if __name__ == "__main__":
    """Load in the data, adjust it to the state before the computer caught fire,
    then run the opcode and print the value in position 0 to the screen.
    """
    instruction_tuple = load_input_data('day03/input.txt')
    (fewest_crossover,
     fewest_steps0,
     fewest_steps1) = get_fewest_steps_to_intersec(instruction_tuple)
    fewest_steps_tot = fewest_steps0 + fewest_steps1

    print('\n---- Day 3, Puzzle 2 ----')
    print(f'Fewest combined steps: {fewest_steps_tot} ' +
          f'at cross over point {fewest_crossover}')
