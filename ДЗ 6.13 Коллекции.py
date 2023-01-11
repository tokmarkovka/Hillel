# *13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках, но в каждой
#  ТОЛЬКО ПО ОДНОМУ разу. Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"],
#   т.к. эти символы есть в каждой строке по одному разу

my_first_string = 'aaaasdf1'
my_second_string = 'asdfff2'

# создадим два списка и при помощи циклов, добавим в каждый список только те элементы, которые повторяются один раз
# в каждой строке

my_first_list = []
my_second_list = []

for element in my_first_string:
    if my_first_string.count(element) == 1:
        my_first_list.append(element)
    else:
        continue

print('my_first_list', my_first_list)

for element in my_second_string:
    if my_second_string.count(element) == 1:
        my_second_list.append(element)
    else:
        continue

print('my_second_list', my_second_list)

# затем создадим список, преобразовав списки в множества, чтобы найти общие элементы

print('Список символов, которые повторяются в строках один раз: ', list(set(my_first_list) & set(my_second_list)))


# варианты, расмотренные на практике

# my_str1 = 'aaaasdf1'
# my_str2 = 'asdfff2'
# # print(list(set(my_str1).intersection(set(my_str2))))
# li1 = [i for i in my_str1 if my_str1.count(i) == 1]
# li2 = [i for i in my_str2 if my_str2.count(i) == 1]
# print(li1, li2)
# print(set(li1) & set(li2))
# li = set([i for i in my_str1 if my_str1.count(i) == 1]) & set([i for i in my_str2 if my_str2.count(i) == 1])
