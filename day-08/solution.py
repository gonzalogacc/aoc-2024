from collections import namedtuple
from copy import deepcopy
from itertools import permutations


def read_data(input_file: str) -> list:
    data = []
    with open(input_file) as ifile:
        for line in ifile:
            data.append(list(line.strip()))
    return data


def printm(data):
    print()
    for line in data:
        print(" ".join(line))
    print()


Coords = namedtuple('Coords', 'row col')


def compile_antenas(data):
    antenas = {}
    for r, row in enumerate(data):
        for c, antenna in enumerate(row):
            if antenna == '.':
                continue
            if antenna not in antenas:
                antenas[antenna] = []
            antenas[antenna].append(Coords(r, c))
    return antenas


def process_antenna_pair_1(a1, a2, mat_size):
    row_dif = a1.row - a2.row
    col_dif = a1.col - a2.col
    antinode = Coords(a1.row + row_dif, a1.col + col_dif)

    # Check the antinode is within the matrix limits
    if antinode.row < 0 or antinode.row >= mat_size:
        return []
    if antinode.col < 0 or antinode.col >= mat_size:
        return []

    return [antinode, ]


def process_antenna_pair_2(a1, a2, mat_size):
    antinodes = set()
    antinodes.update((a1, a2))
    row_dif = a1.row - a2.row
    col_dif = a1.col - a2.col
    i = 0
    antinode = Coords(a1.row + row_dif, a1.col + col_dif)
    while antinode.row >= 0 and antinode.row < mat_size and antinode.col >= 0 and antinode.col < mat_size:
        antinodes.add(antinode)
        i += 1
        antinode = Coords(a1.row + (row_dif * i), a1.col + (col_dif * i))

    return antinodes


def solution1(data, antena_process_function):
    antennas = compile_antenas(data)
    antinodes = set()
    for freq, antennas in antennas.items():
        for a1, a2 in permutations(antennas, 2):
            antinode = antena_process_function(a1, a2, len(data[0]))
            antinodes.update(antinode)

    # Just to check the antinodes little map :)
    sol_data = deepcopy(data)
    for antinode in antinodes:
        sol_data[antinode.row][antinode.col] = '#'

    return len(antinodes)


def test_solution1():
    data = read_data("sample-data.txt")
    assert solution1(data, process_antenna_pair_1) == 14


def test_solution2():
    data = read_data("sample-data.txt")
    assert solution1(data, process_antenna_pair_2) == 34


if __name__ == "__main__":
    data = read_data('real-data.txt')
    print(solution1(data, process_antenna_pair_1))
    print(solution1(data, process_antenna_pair_2))
