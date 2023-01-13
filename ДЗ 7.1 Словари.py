# 1)Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]

persons = [
    {"name": "John", "age": 15},
    {"name": "Alice", "age": 27},
    {"name": "Mary", "age": 90},
    {"name": "Stacy", "age": 32},
    {"name": "Jack", "age": 15}
]

# а) Создать список и поместить туда имя самого молодого человека.
# Если возраст совпадает - поместить все имена самых молодых.

# list_of_youngest_people = []
# min_age = 300
# for age in persons:
#     if min_age > age['age']:
#         min_age = age['age']
# for age in persons:
#     if min_age == age['age']:
#         list_of_youngest_people.append(age['name'])
# print('Список самых молодых: ', list_of_youngest_people)

min_age = min(age['age'] for age in persons)
print('Минимальный возраст: ', min_age)
list_of_youngest_people = [age['name'] for age in persons if age['age'] == min_age]
print('Список самых молодых: ', list_of_youngest_people)

# б) Создать список и поместить туда самое длинное имя.
# Если длина имени совпадает - поместить все такие имена.

list_of_longest_names = []
longest_name = 0
for l_name in persons:
    if longest_name < len(l_name['name']):
        longest_name = len(l_name['name'])
for l_name in persons:
    if longest_name == len(l_name['name']):
        list_of_longest_names.append(l_name['name'])

print('Максимальная длина имени: ', longest_name)
print('Список самых длинных имен: ', list_of_longest_names)

# в пайтон стайле не получилось

# max_name_len = max(age['age'] for age in persons)
# print('Максимальная длина имени: ', max_name_len)
# list_of_longest_names = [age['name'] for age in persons if age['age'] == max_name_len]
# print('Список самых длинных имен: ', list_of_longest_names)

# в) Посчитать среднее количество лет всех людей из начального списка.

average_age_list = []
for age in persons:
    if age in persons:
        average_age_list.append(age['age'])
print('Список всех возрастов: ', average_age_list)
print('Cреднее количество лет всех людей: ', sum(average_age_list)/len(average_age_list))
print('Cреднее количество полных лет всех людей: ', int(sum(average_age_list)/len(average_age_list)))



# for age in persons:
#     average_number_of_years = sum(persons['age'])

# print(*persons)
# dict_persons = dict(persons)
#
# print('dict_persons', dict_persons['name'])
# list_with_youngest_person = []
# print(persons[-1])
# print(*persons)
# for name in persons:
#     print(age.values(), end=' ')
#
# # list_with_youngest_person.append(persons[])
#
# list_with_longest_name = []
#
# average_age = (sum(persons['age'] for persons))
