import re
from collections import namedtuple


def read_data(input_file: str) -> list:
    data = []
    with open(input_file) as ifile:
        for line in ifile:
            sline = list(line.strip())
            data.append(sline)
    return data


def printm(data):
    print()
    for line in data:
        print(" ".join(map(str, line)))
    print()


Coords = namedtuple('Coords', 'row column')
GuardInfo = namedtuple('GuardPosition', 'coords direction')

def get_guard_info(data):
    pattern = re.compile('[<>^v]')
    for i, line in enumerate(data):
        for match in pattern.finditer(''.join(line)):
            return GuardInfo(Coords(i, match.start()), match.group())
    raise Exception('Guard not found')


def rotate_right(matrix):
    return [list(m[::-1]) for m in zip(*matrix)]


def rotate_left(matrix):
    return [list(m[::]) for m in reversed(list(zip(*matrix)))]


def setup_matrix(matrix):
    """ Setup the initial matrix to make the guard point to the right"""
    turns = {">": 0, "^": 1, "<": 2, "v": 3}
    guard_info = get_guard_info(matrix)
    for x in range(turns[guard_info.direction]):
        matrix = rotate_right(matrix)
    return matrix


def next_step(matrix, guard_coords, path):

    line = matrix[guard_coords.row]
    # If there is, move the guard there and
    try:
        obst_pos = line.index("#", guard_coords.column+1)

    except ValueError as e:
        print(f"Done, guard leaving the area, {guard_coords.row}, {guard_coords.column}, {len(line)}")
        for x in range(guard_coords.column, len(line)):
            # Process is done, guard left the area
            line[x] = "X"
            matrix[guard_coords.row] = line

        printm(matrix)
        new_guard_position = Coords(row=len(line), column=guard_coords.row)
        converted_path = [Coords(row=len(line) - coord.column, column=coord.row) for coord in path]
        converted_path.append(new_guard_position)
        return matrix, None, converted_path


    for x in range(guard_coords.column, obst_pos):
        line[x] = "X"
    matrix[guard_coords.row] = line
    # printm(matrix)

    # Update the new position, the row is how far the thing is from the last position, the new column is the row
    new_guard_position = Coords(row=len(line)-obst_pos, column=guard_coords.row)
    converted_path = [Coords(row=len(line)-coord.column, column=coord.row) for coord in path]
    converted_path.append(new_guard_position)

    # First rotate matrix
    matrix = rotate_left(matrix)
    # print(f"--> {obst_pos} {new_guard_position}")

    return matrix, new_guard_position, converted_path


def solution1(data):
    # Get the guard info and get the matrix pointing the right way
    guard_info = get_guard_info(data)
    data = setup_matrix(data)

    # Get the guard info again because the matrix might have been rotated
    guard_info = get_guard_info(data)
    guard_position = guard_info.coords
    path = []
    while guard_position is not None:
        data, guard_position, path = next_step(data, guard_position, path)

    total = 0
    for line in data:
        total += line.count('X')

    return total, data


def solution2(data):
    _, data = solution1(data)
    printm(data)
    return None


def test_solution1():
    data = read_data("sample-data.txt")
    assert solution1(data)[0] == 41


def test_solution2():
    data = read_data("sample-data.txt")
    assert solution2(data) == 6


if __name__ == "__main__":
    data = read_data('real-data.txt')
    print(solution1(data))
    print(solution2(data))
