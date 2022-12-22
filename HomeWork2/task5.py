# Задача 5
# Реализуйте алгоритм перемешивания списка.

import random

my_list = [2, -4, 33, 7, 15, 22]

my_mess = my_list[:]

my_len = len(my_mess)
for element in range(my_len):
    index = random.randint(0, my_len - 1)
    temp = my_mess[index]
    my_mess[index] = my_mess[element]
    my_mess[element] = temp

print(f'before {my_list}')
print(f'after  {my_mess}')