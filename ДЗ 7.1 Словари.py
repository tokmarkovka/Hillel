# 1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
#     а) Создать список и поместить туда имя самого молодого человека.
#         Если возраст совпадает - поместить все имена самых молодых.
#     б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
#     в) Посчитать среднее количество лет всех людей из начального списка.

persons = [
    {"name": "John", "age": 15},
    {"name": "Alice", "age": 27},
    {"name": "Mary", "age": 90},
    {"name": "Stacy", "age": 33},
    {"name": "Jack", "age": 45}
]

list_with_youngest_person = []
print(persons[-1])
print(*persons)
# for name in persons:
#     print(age.values(), end=' ')
#
# # list_with_youngest_person.append(persons[])
#
# list_with_longest_name = []
#
# average_age = (sum(persons['age'] for persons))
