# 1) У вас есть список my_list с значениями типа int.
# Распечатать те значения, которые больше 100.
# Задание выполнить с помощью цикла for.

import random

# сгенерируем список из 30 случайных чисел в диапазоне от 1 до 299

my_list = [random.randint(1, 300) for numbers in range(30)]
print('my_list', my_list)
for numbers in my_list:
    if numbers > 100:
        print(numbers, end=' ')
