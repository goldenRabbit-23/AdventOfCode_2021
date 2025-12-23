import sys
from collections import defaultdict, Counter


def main():
    data = open(sys.argv[1]).read().split('\n')
    points = defaultdict(int)

    for line in data:
        s, e = line.split(' -> ')
        x1, y1 = map(int, s.split(','))
        x2, y2 = map(int, e.split(','))

        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2 + step, step):
                points[(x1, y)] += 1
        elif y1 == y2:
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2 + step, step):
                points[(x, y1)] += 1

    overlaps = Counter(points.values())
    print(sum(v for _, v in overlaps.most_common()[1:]))


if __name__ == '__main__':
    main()
