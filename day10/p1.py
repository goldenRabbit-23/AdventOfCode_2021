import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    score = 0

    for line in data:
        stack = []
        for c in line:
            if c in '([{<':
                stack.append(c)
            else:
                opening = stack.pop()
                if (opening, c) in [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]:
                    continue
                else:
                    score += {')': 3, ']': 57, '}': 1197, '>': 25137}[c]
                    break

    print(score)


if __name__ == '__main__':
    main()
