
def read_data(input_file):
    with open(input_file) as ifile:
        list_a = []
        list_b = []
        for line in ifile:
            a, b = map(int, line.strip().split("   "))
            list_a.append(a)
            list_b.append(b)
        list_a.sort()
        list_b.sort()
    return list_a, list_b


def solution1(input_file):
        list_a, list_b = read_data(input_file)
        total_difference = 0
        for pair in zip(list_a, list_b):
            total_difference += max(pair) - min(pair)
        return total_difference


def solution2(input_file):
    list_a, list_b = read_data(input_file)
    return sum([loc_id * list_b.count(loc_id) for loc_id in list_a])


def test_solution():
    assert solution1('sample-data.txt') == 11
    assert solution2('sample-data.txt') == 31


if __name__ == "__main__":
    print(solution1('real-data.txt'))
    print(solution2('real-data.txt'))
