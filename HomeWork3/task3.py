# Задача 3
# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

num = int(input('Введите число: '))

my_list = []

for i in range(num):
    my_list.append(round(random.uniform(1, 100), 2))

my_min = 1000;
my_max = -1000;

for element in my_list:
    if my_min > element % 1:
        my_min = element % 1 
    if my_max < element % 1:
        my_max = element % 1     

print(f'{my_list} => {round(my_max - my_min, 2)}')
