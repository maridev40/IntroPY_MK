# Задача 2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random, math

num = int(input('Введите число: '))

my_list = []
for element in range(num):
    my_list.append(random.randint(1, num))

my_couple = []
for i in range(0, math.ceil(num / 2)):
    my_couple.append(my_list[i] * my_list[num - 1 - i])

print(f'{my_list} => {my_couple}')    