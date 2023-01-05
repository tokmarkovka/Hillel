# *6. Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел).
#  Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
# 	- Примечание. Эту задачу можно решить в одну строчку.

import random

# сгенерируем список из 10 случайных чисел в диапазоне от 1 до 19

my_first_list = [random.randint(1, 20) for numbers in range(10)]
my_second_list = [random.randint(1, 20) for numbers in range(10)]

print('my_first_list', my_first_list)
print('my_second_list', my_second_list)

print(len(set(my_first_list) & (set(my_second_list))))

