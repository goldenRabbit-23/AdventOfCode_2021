import sys
from collections import deque, Counter
from itertools import combinations


ORIENTATIONS = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-z, -y, -x),
]

def main():
    data = open(sys.argv[1]).read().split('\n\n')

    scanners = []
    for section in data:
        lines = section.split('\n')[1:]
        coords = [tuple(map(int, line.split(','))) for line in lines]
        scanners.append(coords)

    q = deque([0])
    remaining = set(range(1, len(scanners)))
    scanner_positions = [(0, 0, 0)]

    while q:
        current = q.popleft()
        current_beacons = scanners[current]

        for other in list(remaining):
            other_beacons = scanners[other]

            for orient in ORIENTATIONS:
                oriented = [orient(x, y, z) for x, y, z in other_beacons]
                deltas = Counter()

                for bx, by, bz in current_beacons:
                    for ox, oy, oz in oriented:
                        deltas[(bx - ox, by - oy, bz - oz)] += 1

                delta, count = deltas.most_common(1)[0]
                if count >= 12:
                    dx, dy, dz = delta
                    transformed = [(ox + dx, oy + dy, oz + dz) for ox, oy, oz in oriented]
                    scanners[other] = transformed
                    remaining.remove(other)
                    q.append(other)
                    scanner_positions.append((dx, dy, dz))
                    break

    max_dist = 0
    for (x1, y1, z1), (x2, y2, z2) in combinations(scanner_positions, 2):
        max_dist = max(max_dist, abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2))

    print(max_dist)


if __name__ == '__main__':
    main()
