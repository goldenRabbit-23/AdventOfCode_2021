import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    numbers = [int(line) for line in data]
    current = numbers[0]
    increase_count = 0

    for number in numbers[1:]:
        if number > current:
            increase_count += 1
        current = number

    print(increase_count)


if __name__ == '__main__':
    main()
