import sys


def main():
    data = open(sys.argv[1]).read()
    raw_packets = bin(int(data, 16))[2:].zfill(len(data) * 4)

    def parse(i):
        version = int(raw_packets[i:i+3], 2)
        type_id = int(raw_packets[i+3:i+6], 2)
        i += 6
        version_sum = version

        if type_id == 4:
            while True:
                group = raw_packets[i:i+5]
                i += 5
                if group[0] == '0': break
        else:
            if raw_packets[i] == '0':
                length = int(raw_packets[i+1:i+16], 2)
                i += 16
                target = i + length
                while i < target:
                    sub_version_sum, i = parse(i)
                    version_sum += sub_version_sum
            else:
                count = int(raw_packets[i+1:i+12], 2)
                i += 12
                for _ in range(count):
                    sub_version_sum, i = parse(i)
                    version_sum += sub_version_sum

        return version_sum, i

    print(parse(0)[0])


if __name__ == '__main__':
    main()
