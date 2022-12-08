print('Задание 4*\n')
# Создайте приложение подбирающее правильное окончание к фразе: "Маша нашла
# в лесу {К} гриб...". K пользователь вводит с клавиатуры.
# Например: Маша нашла в лесу 7 грибОВ.
# Маша нашла в лесу 32 грибА.


mushrooms = int(input('Привет, Машенька! Напиши, сколько грибов собрала в лесу:'))
ending_of_word = str()

# если количество грибов заканчивается в промежутке с 11 до 19 включительно:

if 10 < mushrooms < 20 or 10 < mushrooms % 100 < 20:
    ending_of_word = 'ов'

# прописываем правила для последней цифры числа за исключением окончаний 11-19:

elif mushrooms == 1:
    ending_of_word = ''
elif mushrooms % 10 == 2 or mushrooms % 10 == 3 or mushrooms % 10 == 4:
    ending_of_word = 'а'
else:
    ending_of_word = 'ов'

print(f'Поздравляем, ты собрала {mushrooms} гриб{ending_of_word}!')
