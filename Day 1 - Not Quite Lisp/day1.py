def main():
    input = open('./input.txt')
    instructions: str = input.read()
    floor: int = 0

    for instruction in instructions:
        match instruction:
            case '(':
                floor += 1
            case ')':
                floor -= 1

    print(f'Floor: {floor}')

    input.close()


if __name__ == '__main__':
    main()
