# Задача 4
# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

num = int(input('Введите натуральную степень: '))

polyn = ''
with open('file.txt', 'w') as data:

    for k in range(num, 0, -1):
        my_power = 'x**' + str(k)
        if k == 1:
            my_power = 'x'
        koef = random.randint(0, 100)
        if koef != 0:
            if koef == 1:
                koef = ''
            else:
                koef = str(koef) + '*'
            if len(polyn) > 0:
                polyn += ' + ' + str(koef) + my_power
            else:
                polyn += str(koef) + my_power
    if len(polyn) > 0:
        koef = random.randint(0, 100)
        polyn += ' + ' + str(koef) + ' = 0'
        data.write(f'{polyn}\n')
                                                     