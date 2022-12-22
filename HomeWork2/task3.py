# Задача 3
# Задайте список из n чисел последовательности
#  (1 + 1\n)^n и выведите на экран их сумму.

num = int(input('Введите число: '))

my_dict = {}

for element in range(1, num + 1):
    my_dict[element] = round((1 + 1 / element) ** element, 2)

print(f'Для n={num} {my_dict}')

sum = 0
for  index in my_dict:
    sum += my_dict[index]

print(f'Сумма {sum}')    