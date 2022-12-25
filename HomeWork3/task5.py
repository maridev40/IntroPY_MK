# Задача 5
# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# *Пример:*

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)  

def nfib(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return nfib(n + 2) - nfib(n + 1)

num = int(input('Введите целое число: '))

my_list = []

for element in range(-num, 0, 1):
    my_list.append(nfib(element))

for element in range(0, num + 1):
    my_list.append(fib(element))

print(my_list)