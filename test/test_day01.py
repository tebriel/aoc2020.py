from solutions.day01 import find_match


def test_two():
    numbers = [1721, 979, 366, 299, 675, 1456]
    match = find_match(numbers, 2020)
    assert 299 in match
    assert 1721 in match


def test_three():
    numbers = [1721, 979, 366, 299, 675, 1456]
    match = find_match(numbers, 2020, 3)
    for s in [979, 366, 675]:
        assert s in match
