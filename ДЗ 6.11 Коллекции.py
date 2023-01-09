# 11. Дана строка my_str. Создать список в который поместить те символы из my_str, которые встречаются
# в строке ТОЛЬКО ОДИН раз.

my_str = 'Шла Саша по шоссе 696.'
my_list = []

for symbol in my_str:
    if my_str.count(symbol) > 1:
        continue
    else:
        my_list.append(symbol)

print('Список символов, которые встречаются в строке один раз: ', my_list)
