# Задача 2
# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

def isitPrime(k):
    if k == 2 or k ==3:
        return True
    if k % 2 == 0 or k < 2:
        return False

    for i in range(3, int(k ** 0.5) +1, 2):
        if k % i == 0:
            return False

    return True

num = int(input('Введите число: '))

if isitPrime(num):
    print(f'Число {num} простое число')
else:
    my_list = []
    for i in range(1, num + 1):
        if isitPrime(i):
            if num % i == 0:
                while num % i == 0:
                    my_list.append(i)
                    num /= i
    print(my_list)                 