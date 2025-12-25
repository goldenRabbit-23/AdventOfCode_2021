import sys


def main():
    dots, folds = open(sys.argv[1]).read().split('\n\n')
    dots = {tuple(map(int, line.split(','))) for line in dots.splitlines()}
    axis, value = folds.splitlines()[0].split()[-1].split('=')
    value = int(value)

    if axis == 'x':
        dots = {(x if x < value else 2 * value - x, y) for x, y in dots}
    else:
        dots = {(x, y if y < value else 2 * value - y) for x, y in dots}

    print(len(dots))


if __name__ == '__main__':
    main()
