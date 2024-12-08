from itertools import product


def read_data(input_file: str) -> list:
    data = []
    with open(input_file) as ifile:
        for line in ifile:
            result, raw_inputs = line.strip().split(":")
            input_list = list(map(int, raw_inputs.strip().split(" ")))
            data.append((int(result), input_list))
    return data


def get_operators_combinations(inputs, operations):
    operators_count = len(inputs) - 1
    combinations = product(operations, repeat=operators_count)
    return combinations


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def concatenate(x, y):
    return int(f"{x}{y}")


def process_equation(result, inputs, operations):
    if len(inputs) == 1 and result == inputs[0]:
        return [result]

    combinations = get_operators_combinations(inputs, operations=''.join(operations.keys()))

    good_entries = []
    for combo in combinations:
        total_result = inputs[0]
        for i in range(len(inputs) - 1):
            total_result = operations[combo[i]](total_result, inputs[i + 1])

        if result == total_result:
            good_entries.append(result)
    return good_entries


def analyze_equations(data, operations):
    good_eqs = []
    for i, (result, number_inputs) in enumerate(data):
        good_combos = process_equation(result, number_inputs, operations)
        if good_combos:
            good_eqs.append(i)
    return good_eqs


def solution1(data):
    operations = {
        "+": add,
        "*": multiply
    }
    total_good_lines = sum([data[eq][0] for eq in analyze_equations(data, operations)])
    return total_good_lines


def solution2(data):
    operations = {
        "+": add,
        "*": multiply,
        "|": concatenate
    }
    total_good_lines = sum([data[eq][0] for eq in analyze_equations(data, operations)])
    return total_good_lines


def test_solution1():
    data = read_data("sample-data.txt")
    assert solution1(data) == 3749


def test_solution2():
    data = read_data("sample-data.txt")
    assert solution2(data) == 11387


if __name__ == "__main__":
    data = read_data('real-data.txt')
    print(solution1(data))
    print(solution2(data))
