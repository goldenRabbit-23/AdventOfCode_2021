import sys
from itertools import permutations


def reduce(snailfish_number):
    while True:
        exploded, reduced, _, _ = explode(snailfish_number)
        if exploded:
            snailfish_number = reduced
            continue
        splitted, reduced = split(snailfish_number)
        if splitted:
            snailfish_number = reduced
            continue
        break
    return snailfish_number

def explode(snailfish_number, depth=0):
    if isinstance(snailfish_number, int):
        return False, snailfish_number, None, None
    left, right = snailfish_number
    if depth == 4:
        return True, 0, left, right
    exploded, new_left, add_left_value, add_right_value = explode(left, depth + 1)
    if exploded:
        if add_right_value is not None:
            right = add_left(right, add_right_value)
            add_right_value = None
        return True, [new_left, right], add_left_value, add_right_value
    exploded, new_right, add_left_value, add_right_value = explode(right, depth + 1)
    if exploded:
        if add_left_value is not None:
            left = add_right(left, add_left_value)
            add_left_value = None
        return True, [left, new_right], add_left_value, add_right_value
    return False, snailfish_number, None, None

def split(snailfish_number):
    if isinstance(snailfish_number, int):
        if snailfish_number >= 10:
            left, right = snailfish_number // 2, (snailfish_number + 1) // 2
            return True, [left, right]
        else:
            return False, snailfish_number
    left, right = snailfish_number
    splitted, new_left = split(left)
    if splitted: return True, [new_left, right]
    splitted, new_right = split(right)
    if splitted: return True, [left, new_right]
    return False, snailfish_number

def add_left(snailfish_number, value):
    if isinstance(snailfish_number, int):
        return snailfish_number + value
    left, right = snailfish_number
    return [add_left(left, value), right]

def add_right(snailfish_number, value):
    if isinstance(snailfish_number, int):
        return snailfish_number + value
    left, right = snailfish_number
    return [left, add_right(right, value)]

def magnitude(snailfish_number):
    if isinstance(snailfish_number, int):
        return snailfish_number
    left, right = snailfish_number
    return 3 * magnitude(left) + 2 * magnitude(right)

def main():
    data = open(sys.argv[1]).read().splitlines()
    snailfish_numbers = [eval(line) for line in data]
    max_magnitude = 0

    for a, b in permutations(snailfish_numbers, 2):
        current = reduce([a, b])
        max_magnitude = max(max_magnitude, magnitude(current))

    print(max_magnitude)


if __name__ == '__main__':
    main()
