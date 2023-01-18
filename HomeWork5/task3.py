# Создайте программу для игры в ""Крестики-нолики"".

import random, math

# side = int(input('Введите размер поля: '))
side = 5
if side % 2 == 0:
    print('Введите нечетную разменость')

# leng = int(input('Введите длину фигуры для победы: '))
leng = 3

print(f'игровое поле: {side}:{side}; длина фигуры: {leng}')
print(f'координаты отсчитываются с нуля, например, "01" - 0-й ряд и 1-й столбец')

field = [['_' for i in range(side)] for j in range(side)]

diags = [{1: 0, 2: 0},{1: 0, 2: 0}]

player = random.randint(1, 2)
first_player = player
second_player = 0
if first_player == 1:
    second_player = 2
else:
    second_player = 1    

def printField(first, second):
    tmp_top = ''
    for i in range(side):
        tmp_top += str(i) + ' '
    print('  ' + tmp_top)
    for i in range(side):

        tmp_line = str(i) + ' '
        for j in range(side):
            if field[i][j] == first:
                tmp_line += 'X '
            elif field[i][j] == second:
                tmp_line += '0 '
            else:
                tmp_line += f'{field[i][j]} '

        print(tmp_line)  

print(f'Первым ходит игрок {first_player}')
printField(first_player, second_player)

def checkStep(player, row, col) -> bool:
    # print(f'row={row}; col={col}')

    tmp = 0
    for line in ('row', 'col'):
        
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
    
    for line in ('diag_down', 'diag_incr'):
        # print(f'52 line={line}; player={player}')
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
                i = side - 1 - (row - (side - 1 - col))
                j = 0
                delta = i 

        tmp = 0
        while delta >= 0:
            # print(f'77 i={i}; j={j}; delta={delta}; num={field[i][j]}') 
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

        if tmp == leng:
            return True

    return False  

def Step(playnum) -> int:
    coords = input(f'{playnum} игрок, введите координаты хода: ')

    if len(coords) != 2:
        return -1
        
    x = int(coords[0])
    y = int(coords[1])

    if x > side - 1 or y > side - 1:
        return -1
    
    if field[x][y] in (1, 2):
        return -1    

    field[x][y] = playnum

    if checkStep(playnum, x, y):
        return 1

    return 0         

win = 0
count = side * side
while count > 0:
    
    step = Step(player)
    if step < 0:
        print(f'{player} игрок, введите координаты хода еще раз')
        continue
    elif step > 0:
        printField(first_player, second_player)
        print(f'{player} ИГРОК ПОБЕДИЛ !!!')
        win = 1
        break;

    printField(first_player, second_player)

    if player == first_player:
        player = second_player
    else:
        player = first_player

    count -= 1

if win == 0:
    print('НИЧЬЯ !!!')