# *7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit и r_limit, которые точно находятся
# этой строке. Причем l_limit левее чем r_limit. В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими
#  символами. my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

# то что у меня получилось))

my_str = input("Введите строку: ")

l_limit = input("Введите левый символ строки: ")
r_limit = input("Введите правый символ строки: ")

sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]
print("_______________")
print(sub_str)

# варианты, расмотренные на практике

# my_str = 'My long string'
# l_limit = "o"
# r_limit = "g"
# sub_str=my_str[my_str.find(l_limit)+1:my_str.rfind(r_limit)]
# print(sub_str)

# ---------

# my_str = 'My long string'
# l_limit = 'o'
# r_limit = 'g'
# sub_str = ''
# for len_l in range(len(my_str)):
#     if my_str[len_l] == l_limit:
#         index_l = len_l + 1
#         break
# for len_r in range(-1, len(my_str)):
#     if my_str[len_r] == r_limit:
#         index_r = len_r
#         break
# sub_str = my_str[index_l:index_r]
# print(sub_str)
