import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    pos1, pos2 = map(int, (data[0].split(': ')[1], data[1].split(': ')[1]))
    score1, score2 = 0, 0
    die = 1
    rolls = 0

    while True:
        move1 = 0
        for _ in range(3):
            move1 += die
            die = die % 100 + 1
        rolls += 3
        pos1 = (pos1 + move1 - 1) % 10 + 1
        score1 += pos1

        if score1 >= 1000:
            print(score2 * rolls)
            break

        move2 = 0
        for _ in range(3):
            move2 += die
            die = die % 100 + 1
        rolls += 3
        pos2 = (pos2 + move2 - 1) % 10 + 1
        score2 += pos2

        if score2 >= 1000:
            print(score1 * rolls)
            break


if __name__ == '__main__':
    main()
