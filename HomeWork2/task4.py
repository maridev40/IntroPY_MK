# Задача 4
# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

num = int(input('Введите число: '))

my_list = []

for element in range(num):
    my_list.append(random.randint(-num, num))

    print(f'{num} -> {my_list}')

    with open('file.txt', 'w') as data:
        for i in range(2):
            pos = random.randint(i, num - 1)
            data.write(f'{pos}\n')

prod = 1
with open('file.txt', 'r') as data:
    for line in data:
        if int (line) < len(my_list):
            print(f'позиция {int(line)}')
            prod *= my_list[int(line)]

print(f'Произведение {prod}')
