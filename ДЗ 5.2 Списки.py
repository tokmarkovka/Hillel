# 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
# Добавить в my_results те значения, которые больше 100.
# Распечатать список my_results.
# Задание выполнить с помощью цикла for.

import random

# сгенерируем список из 25 случайных чисел в диапазоне от 1 до 199

my_list = [random.randint(1, 200) for numbers in range(25)]
my_results = []
print('Начальный список:\n', my_list)

print("Список с значениями, которые больше 100:")
for numbers in my_list:
    if numbers > 100:
        my_results.append(numbers)
print(my_results)
