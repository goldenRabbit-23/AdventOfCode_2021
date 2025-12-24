import sys
from functools import cache


def main():
    data = open(sys.argv[1]).read()
    lanternfish = [int(x) for x in data.split(',')]

    @cache
    def dfs(timer, days_left):
        if days_left <= timer:
            return 1

        total = 1
        days_after_spawn = days_left - timer - 1
        while days_after_spawn >= 0:
            total += dfs(8, days_after_spawn)
            days_after_spawn -= 7

        return total

    print(sum(dfs(fish, 256) for fish in lanternfish))


if __name__ == '__main__':
    main()
