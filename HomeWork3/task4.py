# Задача 4
# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите целое десятичное число: '))
str = format(num, 'b')
print(f'{num} -> {str}')
