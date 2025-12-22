import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    horizontal, depth, aim = 0, 0, 0

    for line in data:
        command, value = line.split()
        value = int(value)

        if command == 'forward':
            horizontal += value
            depth += aim * value
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value

    print(horizontal * depth)


if __name__ == '__main__':
    main()
