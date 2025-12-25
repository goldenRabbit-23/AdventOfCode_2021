import sys
from collections import Counter
from functools import cache


def main():
    polymer, rules = open(sys.argv[1]).read().split('\n\n')
    polymer = list(polymer)
    rules = dict(line.split(' -> ') for line in rules.splitlines())

    @cache
    def dfs(a, b, step):
        if step == 0: return Counter()
        ins = rules[a + b]
        return Counter({ins: 1}) + dfs(a, ins, step - 1) + dfs(ins, b, step - 1)

    c = Counter()
    for a, b in zip(polymer, polymer[1:]):
        c += Counter({a: 1}) + dfs(a, b, 40)
    c += Counter({polymer[-1]: 1})

    print(c.most_common()[0][1] - c.most_common()[-1][1])


if __name__ == '__main__':
    main()
