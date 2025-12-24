import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    grid = [[int(c) for c in line] for line in data]
    R, C = len(grid), len(grid[0])
    flashes = 0

    for _ in range(100):
        flashed = set()
        for r in range(R):
            for c in range(C):
                grid[r][c] += 1

        while True:
            new_flash = False
            for r in range(R):
                for c in range(C):
                    if grid[r][c] > 9 and (r, c) not in flashed:
                        flashed.add((r, c))
                        flashes += 1
                        new_flash = True
                        for dr, dc in [(-1, -1), (-1, 0), (-1, 1),
                                       ( 0, -1),          ( 0, 1),
                                       ( 1, -1), ( 1, 0), ( 1, 1)]:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < R and 0 <= nc < C:
                                grid[nr][nc] += 1
            if not new_flash:
                break

        for r, c in flashed:
            grid[r][c] = 0

    print(flashes)


if __name__ == '__main__':
    main()
