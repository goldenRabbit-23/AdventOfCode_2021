import sys
import re


def main():
    data = open(sys.argv[1]).read()
    pattern = re.findall(r'(-?\d+)', data)
    _, _, ty1, _ = map(int, pattern)

    max_vy = -ty1 - 1
    print(max_vy * (max_vy + 1) // 2)


if __name__ == '__main__':
    main()
