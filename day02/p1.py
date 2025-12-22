import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    horizontal, depth = 0, 0

    for line in data:
        command, value = line.split()
        value = int(value)

        if command == 'forward':
            horizontal += value
        elif command == 'down':
            depth += value
        elif command == 'up':
            depth -= value

    print(horizontal * depth)


if __name__ == '__main__':
    main()
