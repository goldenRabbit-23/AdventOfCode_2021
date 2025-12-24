import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    unique_count = 0

    for line in data:
        _, output = line.split(' | ')
        output = output.split()
        unique_count += sum(1 if len(value) in {2, 3, 4, 7} else 0 for value in output)

    print(unique_count)


if __name__ == '__main__':
    main()
