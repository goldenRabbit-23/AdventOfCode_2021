import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    grid = [[int(c) for c in line] for line in data]
    R, C = len(grid), len(grid[0])
    risk_level = 0

    for r in range(R):
        for c in range(C):
            if all(
                grid[r][c] < grid[r + dr][c + dc]
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= r + dr < R and 0 <= c + dc < C
            ):
                risk_level += grid[r][c] + 1

    print(risk_level)


if __name__ == '__main__':
    main()
