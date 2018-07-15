questions =[
    'введите первое число: ',
    'введите второе число: ',
    'введите третье число: '
]

numbers = [int(input(x)) for x in questions]

print(f'среднее число среди трех введенных это {numbers[1]}')

#for pull request