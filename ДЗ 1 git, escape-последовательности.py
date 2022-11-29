print('Задание 3\n')
# Вывести в консоли

first_print = 'import antigravity'
second_print = 'import __hello__'
third_print = 'from __future__ import braces'

print(first_print, second_print, third_print, sep='\n')
print('\n')

print('Задание 4\n')
# Вывести на консоль своё имя, нарисованное 'звёздочками'. Для выполнения этого задания надо
# использовать не только символы звёздочки и пробела, но и ESCAPE символы: \n и \t

my_awesome_name = ' ***   *   *  *****\t *****\t*\t\t *\t  *\t  *\t   *\t' \
                  '\n*\t*  *   *  *\t  *\t   *\t*\t\t* *\t  *\t  *\t  *\t*\t' \
                  '\n*\t   *   *  *\t\t   *\t*\t   *   *  **  *\t *\t *\t' \
                  '\n ***   *   *  ***\t   *\t*\t   *   *  *\t* *\t *\t *\t' \
                  '\n\t*  *   *  *\t\t   *\t*\t   *****  *\t **\t *****\t' \
                  '\n*\t*\t* *\t  *\t  *\t   *\t*\t*  *   *  *\t  *\t *\t *\t' \
                  '\n ***\t *\t  *****\t   *\t*****  *   *  *\t  *\t *\t *\t'
print(my_awesome_name)
print('\n')

print('Задание 5\n')
# программа, которая выводит в консоль таблицу Escape-последовательностей:

print('Escape sequences:')
esc1 = '\\a\t\tBell (alert)'
esc2 = '\\b\t\tBackspace'
esc3 = '\\n\t\tNew line'
esc4 = '\\t\t\tHorizontal tab'
esc5 = '\\\\\t\tBackslash \\'
esc6 = '\\\"\t\tDouble quotation mark \"'
esc7 = "\\\'\t\tSingle quotation mark \'"

print(esc1, esc2, esc3, esc4, esc5, esc6, esc7, sep='\n')
