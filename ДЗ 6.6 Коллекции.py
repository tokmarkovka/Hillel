# *6. Дана строка в которой есть числа (разделяются пробелами). Например "43 больше чем 34, но меньше чем 56".
# Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке. Для данного примера ответ - 133.
# (используйте split и проверку isdigit)

# то что у меня получилось, но без запятой:

my_list = ('43 больше чем 34 но меньше чем 56').split()
total = 0
for i in my_list:
    if i.isdigit():
        total += int(i)
    else:
        continue
print("_______________")
print(f"Сумма всех чисел в этой строке равна {total}")

# не получилось доделать:

# my_string = '43 больше чем 34, но меньше чем 56'
# print('my_string: ', my_string)
#
# my_list = my_string.split(sep=' ')
# print('my_list: ', my_list)
# sum_of_all_numbers = 0
# if my_string.isalnum():
#     sum_of_all_numbers=

# варианты, расмотренные на практике

# my_list = "'43 больше чем 34, но меньше чем 56'"
# my_list_of_numbers =''
# sum_of_numbers = []
# for number in my_list:
#     if number.isdigit():
#         my_list_of_numbers += str(number)
#     else:
#         my_list_of_numbers += ' '
# print('my_list_of_numbers: ', my_list_of_numbers)
# print(sum([int(number) for number in my_list_of_numbers.split()]))
