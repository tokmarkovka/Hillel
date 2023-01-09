# *4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
#  Если my_list [1,2,3,4], то new_list [2,3,4,1]
import copy

my_list = [1, 555, 4, 'Svetlana', 2, [666, 9, 6]]
print('my_list: ', my_list)

# используем метод deepcopy, так как у нас имеется вложенный список и согласно условию меняем элементы в новом списке,
# обращаясь к элементам по индексу

new_list = copy.deepcopy(my_list)
new_list[0], new_list[-1] = new_list[-1], new_list[0]

print('new_list: ', new_list)
