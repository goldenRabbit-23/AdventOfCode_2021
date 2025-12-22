import sys
from collections import Counter


def main():
    data = open(sys.argv[1]).read().splitlines()

    # oxygen generator rating
    data_ = data[:]
    for i in range(len(data_[0])):
        c = Counter(line[i] for line in data_)
        if c['1'] >= c['0']:
            data_ = [line for line in data_ if line[i] == '1']
        else:
            data_ = [line for line in data_ if line[i] == '0']
        if len(data_) == 1:
            break

    oxygen_generator_rating = int(data_[0], 2)

    # CO2 scrubber rating
    data_ = data[:]
    for i in range(len(data_[0])):
        c = Counter(line[i] for line in data_)
        if c['1'] >= c['0']:
            data_ = [line for line in data_ if line[i] == '0']
        else:
            data_ = [line for line in data_ if line[i] == '1']
        if len(data_) == 1:
            break

    co2_scrubber_rating = int(data_[0], 2)

    print(oxygen_generator_rating * co2_scrubber_rating)


if __name__ == '__main__':
    main()
