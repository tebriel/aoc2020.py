#!/usr/bin/env python
"""Solve Day 01 Solutions 1 and 2."""
from typing import List, Tuple
from functools import reduce
from itertools import combinations


def find_match(
    numbers: List[int],
    desired: int,
    count: int = 2
) -> Tuple[int, ...]:
    """Find a combination that has a sum equal to the desired number."""
    for combo in combinations(numbers, count):
        if reduce(lambda x, y: x+y, combo) == desired:
            return combo
    return ()


def main() -> None:
    """Load the input and run the program."""
    numbers = []
    with open('./inputs/day01.txt') as infile:
        for line in infile.readlines():
            numbers.append(int(line))

    match = find_match(numbers, 2020)
    print(match, reduce(lambda x, y: x * y, match))
    match = find_match(numbers, 2020, 3)
    print(match, reduce(lambda x, y: x * y, match))


if __name__ == '__main__':
    main()
