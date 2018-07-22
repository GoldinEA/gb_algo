#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
nums = [random.randint(1,100) for x in range(20)]
id_max = nums.index(max(nums))
id_min = nums.index(min(nums))
print(nums)
print(max(nums), nums.index(max(nums)))
print(min(nums), nums.index(min(nums)))
nums[id_min], nums[id_max] = nums[id_max], nums[id_min]
print(nums)
print(max(nums), nums.index(max(nums)))
print(min(nums), nums.index(min(nums)))










