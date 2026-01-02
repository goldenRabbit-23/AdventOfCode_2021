import sys
from itertools import count


def main():
    data = open(sys.argv[1]).read().splitlines()
    grid = [list(line) for line in data]
    R, C = len(grid), len(grid[0])

    for step in count(1):
        moved = False
        new_grid = [row[:] for row in grid]

        # Move east-facing herd
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '>' and grid[r][(c + 1) % C] == '.':
                    new_grid[r][c] = '.'
                    new_grid[r][(c + 1) % C] = '>'
                    moved = True

        grid = [row[:] for row in new_grid]

        # Move south-facing herd
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'v' and grid[(r + 1) % R][c] == '.':
                    new_grid[r][c] = '.'
                    new_grid[(r + 1) % R][c] = 'v'
                    moved = True

        grid = new_grid

        if not moved:
            print(step)
            break


if __name__ == '__main__':
    main()
