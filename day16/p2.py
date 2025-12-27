import sys
from math import prod


def main():
    data = open(sys.argv[1]).read()
    raw_packets = bin(int(data, 16))[2:].zfill(len(data) * 4)

    def parse(i):
        type_id = int(raw_packets[i+3:i+6], 2)
        i += 6

        if type_id == 4:
            number_bits = ''
            while True:
                group = raw_packets[i:i+5]
                number_bits += group[1:]
                i += 5
                if group[0] == '0': break
            result = int(number_bits, 2)
        else:
            values = []
            if raw_packets[i] == '0':
                length = int(raw_packets[i+1:i+16], 2)
                i += 16
                target = i + length
                while i < target:
                    sub_value, i = parse(i)
                    values.append(sub_value)
            else:
                count = int(raw_packets[i+1:i+12], 2)
                i += 12
                for _ in range(count):
                    sub_value, i = parse(i)
                    values.append(sub_value)

            match type_id:
                case 0: result = sum(values)
                case 1: result = prod(values)
                case 2: result = min(values)
                case 3: result = max(values)
                case 5: result = values[0] > values[1]
                case 6: result = values[0] < values[1]
                case 7: result = values[0] == values[1]

        return result, i

    print(parse(0)[0])


if __name__ == '__main__':
    main()
