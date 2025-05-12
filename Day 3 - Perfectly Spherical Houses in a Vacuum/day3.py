def main():
    input = open('./input.txt')
    instructions = input.read()

    santa_x = 0
    santa_y = 0
    visited_houses = set()

    visited_houses.add((santa_x, santa_y))

    for instruction in instructions:
        match instruction:
            case '^':
                santa_y += 1
            case 'v':
                santa_y -= 1
            case '>':
                santa_x += 1
            case '<':
                santa_x -= 1

        visited_houses.add((santa_x, santa_y))

    print(f'Visited Houses: {len(visited_houses)}')

    input.close()


if __name__ == '__main__':
    main()