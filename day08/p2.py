import sys
from itertools import permutations


SEGMENTS_TO_DIGIT = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9',
}

def main():
    data = open(sys.argv[1]).read().splitlines()
    output_sum = 0

    for line in data:
        patterns, output = line.split(' | ')
        patterns = patterns.split()
        output = output.split()

        for perm in permutations('abcdefg'):
            translation = str.maketrans(''.join(perm), 'abcdefg')
            translated_patterns = [''.join(sorted(p.translate(translation))) for p in patterns]

            if all(tp in SEGMENTS_TO_DIGIT for tp in translated_patterns):
                translated_output = [''.join(sorted(o.translate(translation))) for o in output]
                digits = [SEGMENTS_TO_DIGIT[to] for to in translated_output]
                output_sum += int(''.join(digits))
                break

    print(output_sum)


if __name__ == '__main__':
    main()
