import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    numbers = [int(line) for line in data]
    current = sum(numbers[:3])
    increase_count = 0

    for i in range(1, len(numbers) - 2):
        window_sum = sum(numbers[i:i+3])
        if window_sum > current:
            increase_count += 1
        current = window_sum

    print(increase_count)


if __name__ == '__main__':
    main()
