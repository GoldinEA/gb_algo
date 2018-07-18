number = input('Введите любое число: ')

number_ghz = int(input('введите число частоту которого вы хотите проверить: '))

numbers = [x for x in number if int(x) == number_ghz]
print(f'число {number_ghz} встречается в числе {number}  - {len(numbers)} раз')