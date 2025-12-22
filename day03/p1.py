import sys
from collections import Counter


def main():
    data = open(sys.argv[1]).read().splitlines()
    gamma_rate, epsilon_rate = '', ''

    for bits in zip(*data):
        c = Counter(bits)
        gamma_rate += c.most_common()[0][0]
        epsilon_rate += c.most_common()[-1][0]

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))


if __name__ == '__main__':
    main()
