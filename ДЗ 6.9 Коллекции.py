# *9. Дан список чисел. Определите, сколько в этом списке элементов, которые больше суммы двух своих соседей
#  (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов. Крайние элементы списка никогда не учитываются,
#   поскольку у них недостаточно соседей.
#   Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.


# мой вариант был по такой же схеме, как на практике, поэому доделала свое просто

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
counter = 0
for num in range(1, len(my_list)-1):
    if my_list[num] > (my_list[num - 1] + my_list[num + 1]):
        counter += 1
print('Количество элементов: ', counter)

# вариант в пайтон стайл

# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
# print(sum([1 for i in range(1, len(my_list) - 1) if my_list[i] > (my_list[i - 1] + my_list[i + 1])]))

# вариант из интернета

# from random import randint
#
# my_list = [randint(1, 10) for i in range(10)]
# print(f"""Изначальный список:
# {my_list}""")
#
# result = []
# for j in my_list:
#     k = my_list.index(j)
#     if my_list[0] is j or my_list[-1] is j:
#         pass
#     elif j > (my_list[k - 1] + my_list[k + 1]):
#         result.append(j)
#
# print("_______________")
# print(len(result))
