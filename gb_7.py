questions =[
    'введите первую сторону: ',
    'введите вторую сторону: ',
    'введите третью сторону: '
]

triangle = [int(input(x)) for x in questions]


A = triangle[0]
B = triangle[1]
C = triangle[2]

if A == 0 or B == 0 or C == 0 or A > B + C or B > A + C or C > A + B:
    print('Треугольник не существует')
else:
    if A == B == C:
        print('Треугольник равнобедренный и равносторонний')
    elif A == B or A == C or A == B:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')



