import random
num = random.randint(0,100)
print(num)

def num_pointing(num, num_user):
    if num > num_user:
        return print('введенное число меньше загаданного числа')
    else:
        return print('введенное число больше загаданного числа')


for i in range(1,11):
    user_num = int(input(f'Число загадано, осталось {11-i} попыток: '))
    if user_num == num:
        print('число угадано')
        exit()
    else:
        num_pointing(num, user_num)

print(f'Вы не угадали число - загаданное число - {num}')
