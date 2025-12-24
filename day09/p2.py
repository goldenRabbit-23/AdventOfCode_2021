import sys
from collections import deque
from math import prod


def main():
    data = open(sys.argv[1]).read().splitlines()
    grid = [[int(c) for c in line] for line in data]
    R, C = len(grid), len(grid[0])
    low_points = []

    for r in range(R):
        for c in range(C):
            if all(
                grid[r][c] < grid[r + dr][c + dc]
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
                if 0 <= r + dr < R and 0 <= c + dc < C
            ):
                low_points.append((r, c))

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited = set()
        visited.add((sr, sc))
        basin_size = 0

        while q:
            r, c = q.popleft()
            basin_size += 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if (nr < 0 or nr >= R or nc < 0 or nc >= C) or ((nr, nc) in visited or grid[nr][nc] == 9):
                    continue

                q.append((nr, nc))
                visited.add((nr, nc))

        return basin_size

    basin_sizes = [bfs(r, c) for r, c in low_points]
    print(prod(sorted(basin_sizes)[-3:]))


if __name__ == '__main__':
    main()
