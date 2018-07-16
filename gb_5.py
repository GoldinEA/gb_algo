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
word_1 = input('Введите eще одну букву английского алфавита: ')

def num_in_alphabet(word, alphabet):
    for index, elem in enumerate(alphabet, 1):
        if word == elem:
            print(f'буква {word} находится на {index} месте в алфавите')
            return index

num = num_in_alphabet(word, alphabet)
num_1 = num_in_alphabet(word_1, alphabet)

print(f'количество букв между буквами {word} и {word_1} - {abs(num - num_1)}')

