import sys
import re


def main():
    data = open(sys.argv[1]).read()
    pattern = re.findall(r'(-?\d+)', data)
    tx1, tx2, ty1, ty2 = map(int, pattern)
    count = 0

    for vx in range(1, tx2 + 1):
        for vy in range(ty1, -ty1):
            x, y = 0, 0
            cur_vx, cur_vy = vx, vy
            while x <= tx2 and y >= ty1:
                x += cur_vx
                y += cur_vy
                if tx1 <= x <= tx2 and ty1 <= y <= ty2:
                    count += 1
                    break
                cur_vx = max(0, cur_vx - 1)
                cur_vy -= 1

    print(count)


if __name__ == '__main__':
    main()
