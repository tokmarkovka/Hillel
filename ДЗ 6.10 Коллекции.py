# *10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33] Создать новый список в который поместить только строки из my_list.

my_list = [1, 2, 3, "11", "22", 33]
new_list_with_strings = []

# при помоща цикла проверяем является ли тип элемента строкой, если да - добавляем в список

# for element in my_list:
#     if type(element) == str:
#         new_list_with_strings.append(element)
#     else:
#         continue
#
# print('Новый список, содержащий только строки', new_list_with_strings)

# переделанное в пайтон стайл
# ( добавляем в список элементы, для всех значений в моем списке если тип элемента строка)

print('Новый список, содержащий только строки', [element for element in my_list if type(element) == str])


# варианты, расмотренные на практике

# li = [1, 2, 3, "11", "22", 33]
# new_li = []
# for i in li:
#     # if isinstance(i, str):
#     if type(i) == str:
#         new_li.append(i)
# print(new_li)


# print([i for i in li if isinstance(i, str)])
