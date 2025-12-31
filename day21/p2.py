import sys
from functools import cache


FREQ = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

def main():
    data = open(sys.argv[1]).read().splitlines()
    pos1, pos2 = map(int, (data[0].split(': ')[1], data[1].split(': ')[1]))

    @cache
    def dfs(pos1, pos2, score1, score2, turn):
        if score1 >= 21:
            return (1, 0)
        if score2 >= 21:
            return (0, 1)

        wins1, wins2 = 0, 0
        for move, freq in FREQ.items():
            if turn == 0:
                new_pos1 = (pos1 + move - 1) % 10 + 1
                new_score1 = score1 + new_pos1
                w1, w2 = dfs(new_pos1, pos2, new_score1, score2, 1)
            else:
                new_pos2 = (pos2 + move - 1) % 10 + 1
                new_score2 = score2 + new_pos2
                w1, w2 = dfs(pos1, new_pos2, score1, new_score2, 0)
            wins1 += w1 * freq
            wins2 += w2 * freq
        return (wins1, wins2)

    print(max(dfs(pos1, pos2, 0, 0, 0)))


if __name__ == '__main__':
    main()
