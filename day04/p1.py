import sys


def main():
    order, *boards = open(sys.argv[1]).read().split('\n\n')
    order = list(map(int, order.split(',')))
    boards = [
        [list(map(int, row.split())) for row in board.split('\n')]
        for board in boards
    ]
    check = [[[False] * 5 for _ in range(5)] for _ in range(len(boards))]

    for number in order:
        for b, board in enumerate(boards):
            for r, row in enumerate(board):
                for c, val in enumerate(row):
                    if val == number:
                        check[b][r][c] = True

            for i in range(5):
                if all(check[b][i]) or all(check[b][j][i] for j in range(5)):
                    unmarked_sum = sum(
                        board[r][c]
                        for r in range(5)
                        for c in range(5)
                        if not check[b][r][c]
                    )

                    print(unmarked_sum * number)
                    return


if __name__ == '__main__':
    main()
