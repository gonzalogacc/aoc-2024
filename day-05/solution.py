
def read_data(input_file: str) -> tuple[list, list]:
    order = []
    updates = []
    with open(input_file) as ifile:
        for line in ifile:
            sline = line.strip()
            if len(sline) == 0:
                continue
            if '|' in sline:
                order.append(tuple(map(int, sline.split('|'))))
            else:
                updates.append(list(map(int, sline.split(","))))
    return order, updates


def order_by_page(order_pairs: list[tuple[int, int]], update: list[int]) -> dict[int, dict]:
    page2order = {}
    for first, second in order_pairs:
        if first not in update or second not in update:
            continue

        if first not in page2order:
            page2order[first] = dict(pages_before=[], pages_after=[])
        page2order[first]['pages_after'].append(second)

        if second not in page2order:
            page2order[second] = dict(pages_before=[], pages_after=[])
        page2order[second]['pages_before'].append(first)

    return page2order


def order_update(page_neighbours, update):
    npn = [(k, v['pages_before']) for k, v in page_neighbours.items()]
    return [page for page, _ in sorted(npn, key=lambda x: len(x[1]))]


def solution(orders, updates):
    total_middle_correct = 0
    total_middle_incorrect = 0
    for update in updates:
        page_neighbours = order_by_page(orders, update)
        ordered_update = order_update(page_neighbours, update)
        middle_page = ordered_update[len(update) // 2]
        if update == ordered_update:
            total_middle_correct += middle_page
        else:
            total_middle_incorrect += middle_page

    return total_middle_correct, total_middle_incorrect


def test_solution1_orders():
    order, updates = read_data("sample-data.txt")
    assert solution(order, updates)[0] == 143


def test_solution2():
    order, updates = read_data("sample-data.txt")
    assert solution(order, updates)[1] == 123


if __name__ == "__main__":
    order, updates = read_data('real-data.txt')
    print(solution(order, updates))
