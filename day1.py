from itertools import combinations
from typing import Tuple


def expense_groups(filename: str, size: int) -> tuple[int, ...]:
    with open(filename, 'r') as f:
        nums = list(map(lambda l: int(l.strip()), f.readlines()))

    expense_group = list(combinations(nums, size))

    return list(filter(lambda values: sum(values) == 2020, expense_group))[0]


def part_one(filename: str) -> int:
    a, b = expense_groups(filename, 2)
    return a * b


def part_two(filename: str) -> int:
    a, b, c = expense_groups(filename, 3)
    return a * b * c


if __name__ == '__main__':
    print(part_one('expense.txt'))
    print(part_two('expense.txt'))
