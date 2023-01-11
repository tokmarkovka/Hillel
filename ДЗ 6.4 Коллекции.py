# *4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
#  Если my_list [1,2,3,4], то new_list [2,3,4,1]

# мой вариант

import copy

my_list = [1, 555, 4, 'Svetlana', 2, [666, 9, 6]]
print('my_list: ', my_list)

# используем метод deepcopy, так как у нас имеется вложенный список и согласно условию меняем элементы в новом списке,
# обращаясь к элементам по индексу

new_list = copy.deepcopy(my_list)
new_list[0], new_list[-1] = new_list[-1], new_list[0]

print('new_list: ', new_list)

# варианты, расмотренные на практике

# my_list = [1, 555, 4, 'Svetlana', 2, [666, 9, 6]]
# new_list = []
# for i in my_list:
#     new_list.append(i)
# new_list.append(new_list.pop(0))
# print(new_list)

#  ------
# new_list = my_list[1:] + my_list[0:1]
# print(new_list)
