
def read_data(input_file: str) -> list[str]:
    data = []
    with open(input_file) as ifile:
        for line in ifile:
            data.append(list(line.strip()))
    return data


def print_array(data: list[list[str]]):
    for line in data:
        print('\t'.join(map(str, line)))


def inside_limits(off_row, off_column, data) -> bool:
    # Assumes square array
    if 0 > off_row or off_row >= len(data):
        return False

    if 0 > off_column or off_column >= len(data[off_row]):
        return False

    return True


def solution1(data: list[list[str]]) -> int:
    patterns = dict(
        fw={
            (0, 1): "M",
            (0, 2): "A",
            (0, 3): "S",
        },
        bw={
            (0, -1): "M",
            (0, -2): "A",
            (0, -3): "S",
        },
        up={
            (-1, 0): "M",
            (-2, 0): "A",
            (-3, 0): "S",
        },
        down={
            (1, 0): "M",
            (2, 0): "A",
            (3, 0): "S",
        },
        urd={
            (-1, 1): "M",
            (-2, 2): "A",
            (-3, 3): "S",
        },
        lrd={
            (1, 1): "M",
            (2, 2): "A",
            (3, 3): "S",
        },
        uld={
            (-1, -1): "M",
            (-2, -2): "A",
            (-3, -3): "S",
        },
        lld={
            (1, -1): "M",
            (2, -2): "A",
            (3, -3): "S",
        },
    )

    found = []
    for row in range(len(data)):
        for column in range(len(data[row])):

            if data[row][column] != "X":
                continue

            for sp, pattern_coords in patterns.items():
                matching = 0
                for spot, letter in pattern_coords.items():
                    # Check if it fits
                    off_row = row + spot[0]
                    off_column = column + spot[1]

                    if not inside_limits(off_row, off_column, data):
                        continue

                    if data[off_row][off_column] == letter:
                        matching += 1

                if matching == 3:
                    found.append((row, column))

    return len(found)


def solution2(data):
    x_patterns = dict(
        one={
            (-1, -1): "M",
            (-1, 1): "M",
            (1, 1): "S",
            (1, -1): "S",
        },
        two={
            (-1, -1): "S",
            (-1, 1): "S",
            (1, 1): "M",
            (1, -1): "M",
        },
        three={
            (-1, -1): "S",
            (-1, 1): "M",
            (1, 1): "M",
            (1, -1): "S",
        },
        four={
            (-1, -1): "M",
            (-1, 1): "S",
            (1, 1): "S",
            (1, -1): "M",
        }
    )

    found = []
    for row in range(len(data)):
        for column in range(len(data[row])):

            if data[row][column] != "A":
                continue

            for sp, pattern_coords in x_patterns.items():
                matching = 0
                for spot, letter in pattern_coords.items():
                    # Check if it fits
                    off_row = row + spot[0]
                    off_column = column + spot[1]

                    if not inside_limits(off_row, off_column, data):
                        continue

                    if data[off_row][off_column] == letter:
                        matching += 1

                if matching == 4:
                    found.append((sp, row, column))

    return len(found)


def test_solution1():
    data = read_data("sample-data.txt")
    assert solution1(data) == 18


def test_solution2():
    data = read_data("sample-data.txt")
    assert solution2(data) == 9


if __name__ == "__main__":
    data = read_data('real-data.txt')
    print(solution1(data))
    print(solution2(data))
