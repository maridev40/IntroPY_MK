# Создайте программу для игры в ""Крестики-нолики"".

import random

side = int(input('Введите длину стороны поля: '))
# side = 5

leng = int(input('Введите длину фигуры для победы: '))
# leng = 3

autoPlay = input('Включить АВТО ход игроков y/n: ').lower() == 'y'
# autoPlay = True

print(f'игровое поле: {side}:{side}; длина фигуры: {leng}')
print(f'координаты отсчитываются с нуля и разделяются пробелом, например, "0 1" - 0-й ряд и 1-й столбец')

field = [['_' for i in range(side)] for j in range(side)]

player = random.randint(1, 2)
first_player = player
second_player = 0
if first_player == 1:
    second_player = 2
else:
    second_player = 1    

# Функция определяет символ которым ходит игрок
# возвращает символ, который привязан к игроку для хода
def getPlayerSymbol(player) -> str:
    if player == first_player:
        return 'X'
    else:
        return '0'

# Функция вывода игрового поля
def printField(first, second):
    
    tmp_top = ''
    for i in range(side):
        tmp_top += str(i).ljust(len(str(i)) + 1)
    print(' '.rjust(len(str(side))) + tmp_top)

    for i in range(side):
        tmp_line = str(i).ljust(len(str(side)))
        for j in range(side):
            if field[i][j] == first:
                tmp_line += getPlayerSymbol(first).ljust(len(str(j)) + 1) # X
            elif field[i][j] == second:
                tmp_line += getPlayerSymbol(second).ljust(len(str(j)) + 1) # 0
            else:
                tmp_line += f'{field[i][j]}'.ljust(len(str(j)) + 1)
        print(tmp_line)  

print(f'Первым ходит игрок {first_player}')
printField(first_player, second_player)

# Функция проверки хода на выигрыш
# возвращает True - ход победный; False - ход не победный
def checkWinStep(player, row, col) -> bool:

    # проверить по горизонтали и вертикали
    for line in ('row', 'col'):
        tmp = 0
        # print(f'58 line={line}; player={player}')
        for i in range(side):
            if line == 'row':
                num = field[row][i]
            else:
                num = field[i][col]
            if num == player:
                tmp += 1
                if tmp == leng:
                    break
            else:
                tmp = 0
        if tmp == leng:
            return True 
    
    # проверить по диагоналям
    for line in ('diag_down', 'diag_incr'):
        # print(f'74 row={row}; col={col}; line={line}; player={player}')
        if line == 'diag_down':
            if col >= row:
                i = 0
                j = col - row
                delta = side - 1 - j 
            else:
                i = row - col
                j = 0
                delta = side - 1 - i
            
        else:
            if (side - 1 - col) >= row:
                i = 0
                j = side - 1 - ((side - 1 - col) - row)
                delta = j 
            else:
                i = row - (side - 1 - col)
                j = side - 1
                delta = side - 1 - i 

        tmp = 0
        while delta >= 0:
            # print(f'97 i={i}; j={j}; delta={delta}')
            num = field[i][j] 
            if num == player:
                tmp += 1
                if tmp == leng:
                    break
            else:
                tmp = 0
            
            i += 1
            if line == 'diag_down':
                j += 1
            else:
                j -= 1
            delta -= 1
        # print(f'112 tmp={tmp}; leng={leng}')
        if tmp == leng:
            return True

    return False 

# Функция поиска случайных координат хода
# возвращает строку с координатами
def randomInput(player) -> str:
    max = 100
    while max > 0:
        i = random.randint(0, side - 1)
        j = random.randint(0, side - 1)
        if field[i][j] == '_':
            return f'{i} {j}'
        max -= 1

    print('Не удалось рассчитать АВТО ход. Будет сделан ход 0 0') 
    return '0 0'  

# # Функция интеллектуального поиска координат хода
# def intellInput(player) -> str:

# Функция хода игрока с проверкой координат на корректность
# возвращает: -1 - не правильные координаты; 0 - ход сделан; 1 - сделан победный ход
def Step(playnum) -> int:
    if autoPlay:
        coords = randomInput(playnum)
        print(f'АВТО ход {playnum} игрок ({getPlayerSymbol(player)}) = {coords}')
    else:
        coords = input(f'{playnum} игрок, введите координаты хода: ')
        
    my_list = list(map(int, coords.split(' ')))

    if len(my_list) != 2:
        return -1  

    x = int(my_list[0])
    y = int(my_list[1])

    if x > side - 1 or y > side - 1:
        return -1
    
    if field[x][y] in (1, 2):
        return -1    

    field[x][y] = playnum

    if checkWinStep(playnum, x, y):
        return 1

    return 0         

win = 0
count = side * side
# цикл хода игроков 
while count > 0:
    
    step = Step(player)
    # были заданы неправильные координаты
    if step < 0:
        print(f'{player} игрок, введите координаты хода еще раз')
        continue
    # был сделан победный ход
    elif step > 0:
        printField(first_player, second_player)
        print(f'{player} ИГРОК ({getPlayerSymbol(player)}) ПОБЕДИЛ !!!')
        win = 1
        break;

    printField(first_player, second_player)

    # сменить игрока для следующего хода
    if player == first_player:
        player = second_player
    else:
        player = first_player

    count -= 1

# сделаны все ходы, но победного не было
if win == 0:
    print('НИЧЬЯ !!!')