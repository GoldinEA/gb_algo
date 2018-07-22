#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

num_list = [x for x in range(2, 100)]

mult_dict = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

for mult, values in mult_dict.items():
    for num in num_list:
        if num % mult == 0:
            mult_dict[mult].append(num)
    print(f'{len(mult_dict[mult])} чисел кратно {mult}')






