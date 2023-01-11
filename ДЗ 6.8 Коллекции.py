# *8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список. Если строка
#  содержит нечетное количество символов, пропущенный второй символ последней пары должен быть заменен
#  подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_'](используйте срезы длинны 2)

# начиная со строки 20 я не понимаю как из моего полученного списка добавлять элементы по парам
# (хотела перебирать список, пока длина больше или равно 2, добавляя пары первый и второй элемент
# с шагом 2

my_str = 'Шла Саша по шоссе'
my_list_from_string = list(my_str)
print('my_list_from_string: ', my_list_from_string)

my_list = [my_str]
my_list_with_pairs = []
if len(my_str) != 0:
    my_list[-1] = my_list[-1] + '_'

print('my_list: ', my_list)

counter = 0
while len(my_list) >= 2:
    my_list_with_pairs.append(my_list[0] + my_list[1])
    counter += 2

print('my_list_with_pairs: ', my_list_with_pairs)

# варианты, расмотренные на практике

# my_str = 'abcde'
# my_list = ([my_str[i:i + 2] for i in range(0, len(my_str), 2)])
# if len(my_list[-1]) < 2:
#     my_list[-1] += '_'
# print(my_list)



