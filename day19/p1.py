import sys
from collections import deque, Counter


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
    beacons = set(scanners[0])

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
                    beacons |= set(transformed)
                    scanners[other] = transformed
                    remaining.remove(other)
                    q.append(other)
                    break

    print(len(beacons))


if __name__ == '__main__':
    main()
