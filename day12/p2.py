import sys
from collections import defaultdict


def main():
    data = open(sys.argv[1]).read().splitlines()
    cave_map = defaultdict(list)

    for line in data:
        s, e = line.split('-')
        cave_map[s].append(e)
        cave_map[e].append(s)

    def dfs(cave, visited):
        if cave == 'end': return 1
        count = 0
        for neigh in cave_map[cave]:
            if neigh == 'start': continue
            if neigh.isupper() or visited[neigh] == 0 or (visited[neigh] == 1 and 2 not in visited.values()):
                visited[neigh] += int(neigh.islower())
                count += dfs(neigh, visited)
                visited[neigh] -= int(neigh.islower())
        return count

    print(dfs('start', defaultdict(int)))


if __name__ == '__main__':
    main()
