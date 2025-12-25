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
            if neigh.islower() and neigh in visited: continue
            count += dfs(neigh, visited | {cave} if cave.islower() else visited)
        return count

    print(dfs('start', set()))


if __name__ == '__main__':
    main()
