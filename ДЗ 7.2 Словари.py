# 2)Даны два словаря my_dict_1 и my_dict_2.
#     а) Создать список из ключей, которые есть в обоих словарях.
#     б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
#     в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
#     г) Объединить эти два словаря в новый словарь по правилу:
#         если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#         если ключ есть в двух словарях -
#         поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#         {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

my_dict_1 = {1: 1, 2: 2, 3: 33, 4: 55, 5: 666}
my_dict_2 = {11: 11, 2: 22, 33: 3, 4: 44, 5: 555}

# а) Создать список из ключей, которые есть в обоих словарях.

# 1 - рабочий но оч длинный

first_list_of_keys = []
second_list_of_keys = []
for key in my_dict_1:
    first_list_of_keys.append(key)
for key in my_dict_2:
    second_list_of_keys.append(key)

print('Списки из ключей: ', first_list_of_keys, second_list_of_keys)

list_from_same_keys = []
for key in first_list_of_keys:
    if key == key in second_list_of_keys:
        list_from_same_keys.append(key)
#
print('Cписок из ключей, которые есть в обоих словарях: ', list_from_same_keys)

# 2 - в одну строчку

print('Cписок из ключей, которые есть в обоих словарях: ', list((my_dict_1.keys()) & (my_dict_2.keys())))

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

# 1 - списки берем из первого задания

list_of_keys_from_first_list = []
for key in first_list_of_keys:
    if key not in second_list_of_keys:
        list_of_keys_from_first_list.append(key)

print('Cписок из ключей, которые есть в первом, но нет во втором словаре: ', list_of_keys_from_first_list)

# 2 - в одну строку

list_of_keys_from_first_list = [key for key in list(my_dict_1.keys()) if key not in list(my_dict_2.keys())]
print('Cписок из ключей, которые есть в первом, но нет во втором словаре: ', list_of_keys_from_first_list)

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом,
# но нет во втором словаре.

new_dict = dict()
for key in my_dict_1:
    if key not in second_list_of_keys:
        new_dict[key] = my_dict_1[key]

print('Новый словарь из пар {ключ:значение}: ', new_dict)

# г) Объединить эти два словаря в новый словарь по правилу:
#    если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#    если ключ есть в двух словарях -
#    поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#    {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

# создаем словарь, первім циклом перебираем ключи первого словаря
# ( если ключа нет в первом словаре, добавляем пару ключ:значение в наш новый словарь,
# если ключ из первого словаря есть во втором словаре, добавляем значение для этого ключа
# из второго словаря вместе с первым значением списком к общему ключу в наш словарь)
# вторым циклом перебираем ключи из второг словаря и если их нет в первом, добавляем пару в наш словарь


new_dict_rules = {}
for key in my_dict_1:
    if key not in my_dict_2:
        new_dict_rules[key] = my_dict_1[key]
    elif key in my_dict_2:
        new_dict_rules[key] = [my_dict_1[key], my_dict_2[key]]
for key_2 in my_dict_2:
    if key_2 not in my_dict_1:
        new_dict_rules[key_2] = my_dict_2[key_2]

print('Новый словарь по правилам: ', new_dict_rules)


# скопировала себе ваше решение

# from copy import deepcopy
#
# di1 = {1: 1, 2: 2}
# di2 = {11: 11, 2: 22}
# # глубокая копия первого словаря
# result = deepcopy(di1)
# # перебтраем ключи второго словаря
# for key in di2.keys():
#     # если ключ второго словаря уже есть в результирующем словаре
#     if key in result.keys():
#         # обновляем запись в результирующем словаре, в качестве значения указіваем список из двух єлементов
#         result[key] = list((result[key], di2[key]))
#     else:
#         # иначе добавляем ключ:значение из второго словаря
#         result.update({key: di2[key]})
# print(result)