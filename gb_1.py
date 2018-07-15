
number = input('Введите число: ')
mult = 1
addict = 0
for elem in number:
    mult *= int(elem)
    addict += int(elem)

print(f'Произведение введенных чисел равно: {mult}')
print(f'Сумма введенных чисел равна: {addict}')

