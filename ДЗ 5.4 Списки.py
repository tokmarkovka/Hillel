# *4. Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k,
# сдвинув влево все элементы, стоящие правее элемента с индексом k.

# 	- Программа получает на вход список (можно сгенерировать при помощи генератора случайных чисел),
# затем число k. Программа сдвигает все элементы, а после этого удаляет последний элемент списка при
# помощи метода pop() без параметров.

# 	- Программа должна осуществлять сдвиг непосредственно в списке,
# а не делать это при выводе элементов. Также нельзя использовать дополнительный список.
# Также не следует использовать метод pop(k) с параметром или оператор del.

import random

# сгенерируем список из 7 случайных чисел в диапазоне от 1 до 199

my_list = [random.randint(1, 200) for numbers in range(7)]

# генерируем случайный индек (k)

k = random.randrange(0, 7)

print(my_list)
print(k)

# все элементы, начиная с элемента, имеющего индекс k, заканчивая последним, меняем на те же элементы, начиная
# со следующего элемента после k и до конца

my_list[k:len(my_list)] = my_list[k+1:len(my_list)]
print(my_list)

# удаляем последний єлемент списка

my_list.pop()
print(my_list)

