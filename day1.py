from itertools import combinations


def part_one(filename: str) -> int:
    with open(filename, 'r') as f:
        nums = list(map(lambda l: int(l.strip()), f.readlines()))

    def sum_to_2020(values):
        return sum(values) == 2020

    expense_pairs = list(combinations(nums, 2))

    a, b = list(filter(sum_to_2020, expense_pairs))[0]

    return a * b


def part_two(filename: str) -> int:
    with open(filename, 'r') as f:
        nums = list(map(lambda l: int(l.strip()), f.readlines()))

    def sum_to_2020(values):
        return sum(values) == 2020

    expense_pairs = list(combinations(nums, 3))

    a, b, c = list(filter(sum_to_2020, expense_pairs))[0]

    return a * b * c


if __name__ == '__main__':
    print(part_two('expense.txt'))
