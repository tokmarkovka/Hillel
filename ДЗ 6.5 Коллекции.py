# *5. Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
# Пересоздавать список нельзя! (используйте метод pop)

my_list = [1, 555, [666, 9, 6], 'Svetlana', 2, 4]
print('my_list: ', my_list)

# 1. используя метод pop

my_list.append(my_list.pop(0))
print('my_list, при помощи pop: ', my_list)

# 2. из получившегося списка меняем элементы местами, обращаясь к их индексам

my_list[0], my_list[-1] = my_list[-1], my_list[0]
print('my_list с заменой значений по индексам: ', my_list)
