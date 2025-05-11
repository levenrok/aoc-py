import hashlib


def find_lowest(secret_key) -> int:
    number = 1
    prefix = '00000'

    while True:
        input_hash = f'{secret_key}{number}'

        encoded_string = input_hash.encode()
        hashed_string = hashlib.md5(encoded_string).hexdigest()
        if hashed_string.startswith(prefix):
            print(f'Hashed_String: {hashed_string}')
            return number

        number += 1


def main():
    secret_key = input('Secret Key: ')

    lowest_number = find_lowest(secret_key)
    print(f'Lowest Positive Integer: {lowest_number}')


if __name__ == '__main__':
    main()