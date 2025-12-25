import sys


def main():
    dots, folds = open(sys.argv[1]).read().split('\n\n')
    dots = {tuple(map(int, line.split(','))) for line in dots.splitlines()}
    folds = [line.split()[-1].split('=') for line in folds.splitlines()]

    for axis, value in folds:
        value = int(value)
        if axis == 'x':
            dots = {(x if x < value else 2 * value - x, y) for x, y in dots}
        else:
            dots = {(x, y if y < value else 2 * value - y) for x, y in dots}

    max_x = max(x for x, y in dots)
    max_y = max(y for x, y in dots)

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print('#' if (x, y) in dots else ' ', end='')
        print()


if __name__ == '__main__':
    main()
