import sys


def main():
    enhancement, image = open(sys.argv[1]).read().split('\n\n')
    image = image.split('\n')

    lit_pixels = {
        (r, c)
        for r, row in enumerate(image)
        for c, pxl in enumerate(row)
        if pxl == '#'
    }

    min_r, max_r = 0, len(image) - 1
    min_c, max_c = 0, len(image[0]) - 1

    background = '.'
    for _ in range(2):
        new_lit_pixels = set()
        for r in range(min_r - 1, max_r + 2):
            for c in range(min_c - 1, max_c + 2):
                binary_str = ''
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        # 1) Check if the pixel is lit inside the known bounds
                        if min_r <= nr <= max_r and min_c <= nc <= max_c:
                            binary_str += '1' if (nr, nc) in lit_pixels else '0'
                        # 2) If outside known bounds, check the background pixel
                        else:
                            binary_str += '1' if background == '#' else '0'
                idx = int(binary_str, 2)
                if enhancement[idx] == '#':
                    new_lit_pixels.add((r, c))
        lit_pixels = new_lit_pixels
        background = enhancement[0] if background == '.' else enhancement[-1]
        min_r -= 1
        max_r += 1
        min_c -= 1
        max_c += 1

    print(len(lit_pixels))


if __name__ == '__main__':
    main()
