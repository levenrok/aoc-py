def calculate_paper(dimensions) -> int:
    paper_amount = 0
    slack_amount = 0
    total_amount = 0

    for dimension in dimensions:
        l = dimension['l']
        w = dimension['w']
        h = dimension['h']

        paper_amount += 2 * (l * w) + 2 * (w * h) + 2 * (l * h)
        slack_amount += min(l * w, w * h, l * h)

    total_amount = paper_amount + slack_amount
    return total_amount


def main():
    input = open('./input.txt')
    dimensions = []


    for line in input:
        cleaned_line = line.rstrip()
        dimension = cleaned_line.split('x')
        if len(dimension) == 3:
                sorted_dimension = {'l': int(dimension[0]), 'w': int(dimension[1]), 'h': int(dimension[2])}
                dimensions.append(sorted_dimension)

    total_wrapping_paper = calculate_paper(dimensions)
    print(f'Wrapping Paper: {total_wrapping_paper} sq ft')

    input.close()


if __name__ == '__main__':
    main()