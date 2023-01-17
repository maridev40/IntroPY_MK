# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

import random

def StartIntellStep(min, max, rest) -> int:   
    return  rest % (min + max)   

def UserStep(min, max, rest, prior) -> int:
    if auto_user == 1:
        temp = max + min - prior

        if temp > rest:
            temp = rest

        print(f'Пользователь ввел количество: {temp}')

    else:
        temp = int(input('Введите количество: '))
        temp2 = temp

        if temp > max:
            temp = max
        elif temp < min:
            temp = min
    
        if temp > rest:
            temp = rest

        if temp != temp2:
            print(f'Пользователь ввел количество: {temp}')
    
    return temp


def BotStep(min, max, rest, prior) -> int:

    if smart_bot == 1:
        temp = max + min - prior
    else:
        temp = random.randint(min, max)
        if temp > rest:
            temp = rest

    print(f'Бот ввел количество: {temp}')

    return temp

player = random.randint(1, 2)

candy = 2021
min_candy = 1 
max_candy = 28
smart_bot = 0  # наделить бота интеллектом
auto_user = 1  # автоматический пользователь с интеллектом
candy_temp = 0

if player == 1:
    print('Первый ходит пользователь')
    if auto_user == 1:
        temp = StartIntellStep(min_candy, max_candy, candy)
        print(f'Пользователь ввел количество: {temp}')
    else:
        temp = UserStep(min_candy, max_candy, candy, 0)
        
    candy -= temp
    candy_temp = temp
else:
    print('Первый ходит бот') 
    
    if smart_bot == 1:
        temp = StartIntellStep(min_candy, max_candy, candy)
        print(f'Бот ввел количество: {temp}')
    else:
        temp = BotStep(min_candy, max_candy, candy, 0)

    candy -= temp
    candy_temp = temp

while candy > 0:

    if player == 1:
        temp = BotStep(min_candy, max_candy, candy, candy_temp)
        player = 2
        candy_temp = temp
    else:
        temp = UserStep(min_candy, max_candy, candy, candy_temp)
        player = 1
        candy_temp = temp

    candy -= temp
    # print(f'осталось {candy}')

if player == 1:
    print('Пользователь выиграл')
else:   
    print('Бот выиграл')    


