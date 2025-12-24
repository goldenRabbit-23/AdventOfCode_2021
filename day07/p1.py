import sys


def main():
    data = open(sys.argv[1]).read()
    positions = [int(x) for x in data.split(',')]

    min_fuel = float('inf')
    min_pos, max_pos = min(positions), max(positions)

    for target in range(min_pos, max_pos + 1):
        fuel = sum(abs(p - target) for p in positions)
        min_fuel = min(min_fuel, fuel)

    print(min_fuel)


if __name__ == '__main__':
    main()
