questions =[
    'введите первое число координаты x: ',
    'введите второе число координаты x: ',
    'введите первое число координаты y: ',
    'введите второе число координаты y: '
]

x = [int(input(x)) for x in questions]

eq1 = x[2] - x[3]
eq2 = x[0] - x[1]
eq3 = x[2] * x[1] - x[0] * x[3]

print('Уравнение')
print(f'{eq1}x + {eq2}y + {eq3}')


