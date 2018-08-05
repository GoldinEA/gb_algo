#2. 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

data = [random.randint(0, 50) for x in range(50)]
print(f'исходный список элементов {data}')


def merge_sort(dt):
    result = []
    if len(dt) < 20:
        return sorted(dt)
    mid = int(len(dt) / 2)
    d = dt
    data_a = merge_sort(d[:mid])
    data_b = merge_sort(dt[mid:])
    i = 0
    j = 0
    while i < len(data_a) and j < len(data_b):
        if data_a[i] > data_b[j]:
            result.append(data_b[j])
            j += 1
        else:
            result.append(data_a[i])
            i += 1
    result += data_a[i:]
    result += data_b[j:]
    return result

print(merge_sort(data))





