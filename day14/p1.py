import sys
from collections import Counter


def main():
    polymer, rules = open(sys.argv[1]).read().split('\n\n')
    polymer = list(polymer)
    rules = dict(line.split(' -> ') for line in rules.splitlines())

    for _ in range(10):
        new_polymer = []
        for a, b in zip(polymer, polymer[1:]):
            new_polymer.append(a)
            new_polymer.append(rules[a + b])
        new_polymer.append(polymer[-1])
        polymer = new_polymer

    c = Counter(polymer)
    print(c.most_common()[0][1] - c.most_common()[-1][1])


if __name__ == '__main__':
    main()
