import re
from math import prod


def read_data(input_file: str) -> list[str]:
    data = []
    with open(input_file) as ifile:
        for line in ifile:
            data.append(line.strip())
    return data


def multiply_match(match: str):
    return prod(map(int, match[4:-1].split(",")))


def process_line(line: str, filter_dos: bool = False) -> int:
    line_total = 0
    regex = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    for m in re.finditer(regex, line):
        if filter_dos and line[:m.span()[1]].rfind("don\'t()") > line[:m.span()[1]].rfind("do()"):
            continue
        match_result = multiply_match(m.group(0))
        line_total += match_result
    return line_total


def solution1(data: list[str]) -> int:
    line = ''.join(data)
    return process_line(line)


def solution2(data: list[str]) -> int:
    line = ''.join(data)
    return process_line(line, filter_dos=True)


def test_solution1():
    data = read_data("sample-data.txt")
    assert solution1(data) == 161


def test_solution2():
    data = read_data("sample-data.txt")
    assert solution2(data) == 48


if __name__ == "__main__":
    data = read_data('real-data.txt')
    print(solution1(data))
    print(solution2(data))
