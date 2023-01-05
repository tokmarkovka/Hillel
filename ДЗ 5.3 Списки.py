# 3) У вас есть список my_list с значениями типа int.
# Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
# Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
# Количество элементов в списке можно получить с помощью функции len(my_list)

import random

# сгенерируем список случайных чисел в диапазоне от 1 до 49 в рандомном количестве єлементов списка от 1 до 5

my_list = [random.randint(1, 50) for numbers in range(random.randint(1, 5))]
print('my_list', my_list)

# определяем длину списка

print('my_list length:', len(my_list))

if len(my_list) < 2:
    my_list.append(0)
    print('Новый список: ', my_list)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
    print('Новый список: ', my_list)
