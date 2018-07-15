year = int(input('Введите год:'))


if year % 4 != 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('год високосный')
        else:
            print('год обычный')
    else:
        print('год обычный')
else:
    print('год високосный')
