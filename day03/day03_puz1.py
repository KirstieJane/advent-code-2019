#! /usr/bin/env python


def manhatten_dist_from_str(instruction_tuple):

    # Split up the first and second instructions
    instruction_str_wire0, instruction_str_wire1 = instruction_tuple

    # Convert the string instructions to lists containing hor and vert
    # integer tuples
    path_list_wire0 = wire_path_str_to_list(instruction_str_wire0)
    path_list_wire1 = wire_path_str_to_list(instruction_str_wire1)

    # Convert these lists of instructions into sets of coordinates through
    # which the wires pass
    wire_coords_wire0 = path_list_to_set(path_list_wire0)
    wire_coords_wire1 = path_list_to_set(path_list_wire1)

    (closest_crossover,
     manhatten_dist) = find_min_manhatten_dist(wire_coords_wire0,
                                               wire_coords_wire1)

    return closest_crossover, manhatten_dist


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
    that the wire follows to individual horizontal and vertical paths.

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


def path_list_to_set(wire_path_list):
    """Convert a set of instructions (as (hor, vert) tuples) into a set of
    coordinates through which the wire moves after starting at origin (0, 0)

    Parameters
    ----------
    wire_path_list : list
        a list of (hor, vert) values that contain the instructions
        for where the wire goes around the grid

    Returns
    -------
    wire_coords : set
        a set of coordinates through which the wire passes
    """
    # Start at 0
    origin = (0, 0)
    start_x, start_y = origin

    # Create an empty set to hold all the coordinates that the wire passes
    # through and then add the origin
    wire_coords = set()
    wire_coords.add(origin)

    # Go through all the steps in the wire_path_list and turn those steps into
    # coordinates saved in the wire_coords set
    for hor_steps, vert_steps in wire_path_list:
        ((start_x, start_y),
         wire_coords) = steps_to_coords(hor_steps, vert_steps,
                                        start_x, start_y,
                                        wire_coords)

    return wire_coords


def steps_to_coords(hor_steps, vert_steps, start_x, start_y, wire_coords):
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
    wire_coords : set
        set of coordinates that the wire passes through

    Returns
    -------
    start_x : int
        x coordinate of end point
        (will be the starting point for the next instruction)
    start_y : int
        y coordinate of end point
        (will be the starting point for the next instruction)
    wire_coords : set
        set of coordinates that the wire passes through
    """
    if hor_steps > 0:
        for x in range(1, hor_steps + 1):
            wire_coords.add((start_x + x, start_y))
    elif hor_steps < 0:
        for x in range(1, (-1) * hor_steps + 1):
            wire_coords.add((start_x - x, start_y))

    if vert_steps > 0:
        for y in range(1, vert_steps + 1):
            wire_coords.add((start_x, start_y + y))
    elif vert_steps < 0:
        for y in range(1, (-1) * vert_steps + 1):
            wire_coords.add((start_x, start_y - y))

    start_x, start_y = start_x + hor_steps, start_y + vert_steps

    return (start_x, start_y), wire_coords


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


def find_min_manhatten_dist(wire_coords0, wire_coords1):
    """Find all the points where two wires cross and calculate the manhatten
    distance for these points. Return the minimum value

    Parameters
    ----------
    wire_coords0 : set
        coordinates that the first wire passes through
    wire_coords1 : set
        coordinates that the second wire passes through

    Returns
    -------
    closest_crossover : tuple
        coordinates of closest cross over point
    manhatten_dist : int
        minimum manhatten distance from origin to the closest crossover point
    """
    wire_coords0.intersection(wire_coords1)

    manhatten_dist_dict = {}
    for x, y in wire_coords0.intersection(wire_coords1):
        if not (x, y) == (0, 0):
            manhatten_dist = abs(x) + abs(y)
            manhatten_dist_dict[(x, y)] = manhatten_dist

    # Get the point where the wires cross that has the smallest
    # manhatten distance
    closest_crossover = min(manhatten_dist_dict, key=manhatten_dist_dict.get)
    manhatten_dist = manhatten_dist_dict[closest_crossover]

    return closest_crossover, manhatten_dist


if __name__ == "__main__":
    """Load in the data, adjust it to the state before the computer caught fire,
    then run the opcode and print the value in position 0 to the screen.
    """
    instruction_tuple = load_input_data('day03/input.txt')
    (closest_crossover,
     manhatten_dist) = manhatten_dist_from_str(instruction_tuple)
    print(f'Minimum manhatten distance of: {manhatten_dist} ' +
          f'at cross over point {closest_crossover}')
