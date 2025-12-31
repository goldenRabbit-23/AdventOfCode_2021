import sys
import re


def main():
    data = open(sys.argv[1]).read().splitlines()
    overlaps = []
    total = 0

    for line in data:
        pattern = re.findall(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', line)
        op, x1, x2, y1, y2, z1, z2 = pattern[0][0], *map(int, pattern[0][1:])

        for ox1, ox2, oy1, oy2, oz1, oz2, o_sign in overlaps[:]:
            ix1, ix2 = max(x1, ox1), min(x2, ox2)
            iy1, iy2 = max(y1, oy1), min(y2, oy2)
            iz1, iz2 = max(z1, oz1), min(z2, oz2)

            if ix1 <= ix2 and iy1 <= iy2 and iz1 <= iz2:
                intersection_volume = (ix2 - ix1 + 1) * (iy2 - iy1 + 1) * (iz2 - iz1 + 1)
                total += -o_sign * intersection_volume
                overlaps.append((ix1, ix2, iy1, iy2, iz1, iz2, -o_sign))

        if op == 'on':
            total += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
            overlaps.append((x1, x2, y1, y2, z1, z2, 1))

    print(total)


if __name__ == '__main__':
    main()
