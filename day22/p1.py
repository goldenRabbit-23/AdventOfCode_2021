import sys
import re


def main():
    data = open(sys.argv[1]).read().splitlines()
    cubes_on = set()

    for line in data:
        pattern = re.findall(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', line)
        op, x1, x2, y1, y2, z1, z2 = pattern[0][0], *map(int, pattern[0][1:])

        for x in range(max(x1, -50), min(x2, 50) + 1):
            for y in range(max(y1, -50), min(y2, 50) + 1):
                for z in range(max(z1, -50), min(z2, 50) + 1):
                    if op == 'on':
                        cubes_on.add((x, y, z))
                    else:
                        cubes_on.discard((x, y, z))

    print(len(cubes_on))


if __name__ == '__main__':
    main()
