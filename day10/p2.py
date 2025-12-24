import sys


def main():
    data = open(sys.argv[1]).read().splitlines()
    completion_scores = []

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
                    break
        else:
            score = 0
            for opening in reversed(stack):
                score *= 5
                score += {'(': 1, '[': 2, '{': 3, '<': 4}[opening]
            completion_scores.append(score)

    print(sorted(completion_scores)[len(completion_scores) // 2])


if __name__ == '__main__':
    main()
