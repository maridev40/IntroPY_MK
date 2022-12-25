# Задача 1
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random

num = int(input('Введите число:'))

my_list = []

for element in range(num):
    my_list.append(random.randint(1, num))

print(f'{my_list}')

sum = 0
for i in range(1, num, 2):
    sum += my_list[i]
    print(f'на позиции [{i}] элемент {my_list[i]}')

print(f'Сумма {sum}')  