import sys


def main():
    data = open(sys.argv[1]).read()
    lanternfish = [int(x) for x in data.split(',')]

    for _ in range(80):
        new_fish = []

        for i in range(len(lanternfish)):
            if lanternfish[i] == 0:
                lanternfish[i] = 6
                new_fish.append(8)
            else:
                lanternfish[i] -= 1

        lanternfish.extend(new_fish)

    print(len(lanternfish))


if __name__ == '__main__':
    main()
