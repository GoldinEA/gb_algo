number = input('Введите любое число')

evens = [num for num in number if int(num) % 2 == 0]
odds = [num for num in number if int(num) % 2 != 0]

print(f'количество четных чисел равно {len(evens)}, количество нечетных чисел равно {len(odds)}')
