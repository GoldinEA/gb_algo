

def plus(num):
    numbers = num.split('+')
    return int(numbers[0]) + int(numbers[1])

def mult(num):
    numbers = num.split('*')
    return int(numbers[0]) * int(numbers[1])

def minus(num):
    numbers = num.split('-')
    return int(numbers[0]) - int(numbers[1])

def division(num):
    numbers = num.split('/')
    return int(numbers[0]) / int(numbers[1])

while True:
    print('для того, чтобы выйти из программы введите 0 и нажмите enter')
    number = input('введите выражение в формате 3+4: ')
    if '+' in number:
        print(plus(number))
        continue
    elif '*' in number:
        print(mult(number))
        continue
    elif '-' in number:
        print(minus(number))
        continue
    elif '/' in number:
        print(division(number))
        continue
    elif number == '0':
        print('Программа завершена')
        break
    else:
        print('Выражение введено некорректно - повторите запрос')
        continue


