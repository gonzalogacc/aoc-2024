import copy

def read_data(input_file):
    levels = []
    with open(input_file) as ifile:
        for line in ifile:
            series = list(map(int, line.strip().split(" ")))
            levels.append(series)
    return levels


def apply_conditions(level):
    steps = list(map(lambda i: level[i] - level[i + 1], range(len(level) - 1)))
    monotonic = sum([1 for step in steps if step > 0]) == len(steps) or sum([1 for step in steps if step < 0]) == len(steps)
    range_check = sum([1 <= abs(step) <= 3 for step in steps]) == len(steps)
    return monotonic and range_check


def solution1(levels):
    safe_series = 0
    for i, level in enumerate(levels):
        if apply_conditions(level):
            safe_series += 1
    return safe_series


def solution2(levels):
    safe_series = 0
    for level in levels:
        if apply_conditions(level):
            safe_series += 1
            continue

        for i in range(len(level)):
            damp_level = copy.deepcopy(level)
            del damp_level[i]
            if apply_conditions(damp_level):
                safe_series += 1
                break

    return safe_series


def test_solution1():
    levels = read_data("sample-data.txt")
    assert solution1(levels) == 2


def test_solution2():
    levels = read_data("sample-data.txt")
    assert solution2(levels) == 4


if __name__ == "__main__":
    levels = read_data('real-data.txt')
    print(solution1(levels))
    print(solution2(levels))
