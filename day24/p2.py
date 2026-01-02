import sys
from z3 import Optimize, Ints, And, sat


def main():
    data = open(sys.argv[1]).read().splitlines()
    program = [data[i:i+18] for i in range(0, len(data), 18)]
    stack = []
    relations = []

    for i, prog in enumerate(program):
        if prog[4].startswith('div z 1'):
            stack.append((i, int(prog[15].split()[-1])))
        else:
            j, c = stack.pop()
            relations.append((i, j, c + int(prog[5].split()[-1])))

    opt = Optimize()
    digits = Ints('d0 d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 d11 d12 d13')
    for d in digits: opt.add(And(d >= 1, d <= 9))
    for i, j, c in relations: opt.add(digits[i] == digits[j] + c)
    for d in digits: opt.minimize(d)

    if opt.check() == sat:
        m = opt.model()
        print(''.join(str(m[d]) for d in digits))


if __name__ == '__main__':
    main()
