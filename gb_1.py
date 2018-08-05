#1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Вывести на экран исходный и отсортированный массивы.
import random

data = [random.randint(-100, 100) for x in range(11)]
print(f'исходный массив  {data}')
n = 1
while n < len(data):
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
    n += 1

print(f'отсортированный массив {data}')






