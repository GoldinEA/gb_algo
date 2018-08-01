#4. Определить, какое число в массиве встречается чаще всего.
from collections import Counter, OrderedDict
import sys
import random



def func_gb4():
    num_list = [random.randint(1,100) for x in range(1, 105)]
    sorted_num_list = OrderedDict(sorted(Counter(num_list).items(), key=lambda num: num[0]))
    print(sys.getsizeof(Counter(num_list), sorted_num_list))


def func_gb_1_1():
    nums_list = [random.randint(1, 100) for x in range(10)]
    index_list = [nums_list.index(x) for x in nums_list if x % 2 == 0]
    print(sys.getsizeof(nums_list, index_list))



func_gb4()
func_gb_1_1()













