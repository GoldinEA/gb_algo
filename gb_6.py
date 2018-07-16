alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

word = input('Введите букву английского алфавита: ')

for index, elem in enumerate(alphabet, 1):
    if word == elem:
        print(f'буква {word} находится на {index} месте в алфавите')

