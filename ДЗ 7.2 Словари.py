# 2)Даны два словаря my_dict_1 и my_dict_2.
#     а) Создать список из ключей, которые есть в обоих словарях.
#     б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
#     в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
#     г) Объединить эти два словаря в новый словарь по правилу:
#         если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
#         если ключ есть в двух словарях -
#         поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#         {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}

my_dict_1 = {1: 1, 2: 2}
my_dict_2 = {11: 11, 2: 22}



# first_list_of_keys = my_dict_1.keys()
# second_list_of_keys = my_dict_2.keys()
#
# print('first_list_of_keys: ', first_list_of_keys)
# print('second_list_of_keys: ', second_list_of_keys)
#
# list_from_keys = []
# for key in my_dict_1:
#     if key in my_dict_1 == key in my_dict_2:
#         list_from_keys.append(key)
# print(list_from_keys)

for key in my_dict_1:
    first_list_of_keys = (my_dict_1[key])
for key in my_dict_2:
    second_list_of_keys = (my_dict_2[key])
print(my_dict_1['key'])
