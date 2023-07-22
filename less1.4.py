# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


CHECK_NORMAL_1 = 4
CHECK_NORMAL_2 = 100
CHECK_NORMAL_3 = 400
START_YEAR = 1582
result = ''
year = int(input('Введите год: '))
if year < START_YEAR:
    result = 'Вы ввели не верную дату'
elif year % CHECK_NORMAL_1:
    result = 'Год обычный'
elif not year % CHECK_NORMAL_2:
    if not year % CHECK_NORMAL_3:
        result = 'Високосный'
    else:
        result = 'Обычный'
else:
    result = 'Високосный'
print(result)