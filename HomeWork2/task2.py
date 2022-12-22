# Задача 2
# Напишите программу, которая принимает на вход
#  число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


num = int(input('Введите число: '))
my_list = []
for element in range(num):
    prod = 1
    
    for prod_element in range(element + 1):
        prod *= prod_element + 1
    
    my_list.append(prod) 

print(f'{num} -> {my_list}')