number = input('Введите любое число: ')
new_numb = (num for num in number[::-1])
new_numb = ''.join(new_numb)
print(f'Обратное число {new_numb}')



