# Задача 3
# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

import random

my_list = [random.randint(1, 5) for i in range(10)]

print(f'{my_list}')

my_dict = {}
for el in my_list:
    my_dict[el] = 0

my_list2 = []
for i in my_dict:
    my_list2.append(i)

print(my_list2)          
