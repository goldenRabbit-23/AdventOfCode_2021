import sys
from heapq import heappush, heappop


def main():
    data = open(sys.argv[1]).read().splitlines()
    grid = [[int(c) for c in line] for line in data]
    R, C = len(grid), len(grid[0])

    new_grid = [[0] * (C * 5) for _ in range(R * 5)]
    for r in range(R * 5):
        for c in range(C * 5):
            val = grid[r % R][c % C] + (r // R) + (c // C)
            new_grid[r][c] = (val - 1) % 9 + 1
    grid = new_grid
    R, C = len(grid), len(grid[0])

    risks = [[float('inf')] * C for _ in range(R)]
    risks[0][0] = 0
    pq = [(0, 0, 0)]

    while pq:
        risk, cr, cc = heappop(pq)
        if (cr, cc) == (R - 1, C - 1):
            print(risk)
            break
        if risk > risks[cr][cc]: continue
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < R and 0 <= nc < C:
                new_risk = risk + grid[nr][nc]
                if new_risk < risks[nr][nc]:
                    risks[nr][nc] = new_risk
                    heappush(pq, (new_risk, nr, nc))


if __name__ == '__main__':
    main()
