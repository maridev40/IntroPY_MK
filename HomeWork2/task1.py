# Задача 1
# Напишите программу, которая принимает на вход вещественное
#  число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите вещественное число: ')

sum = 0
for str in num:
    if str.isdigit():
        sum += int(str)

print(f'{num} -> {sum}')