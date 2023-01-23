# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

my_str = 'WWWffffffffffffhhhhhhhh rrrrrrDDDDDsss'
print(my_str)

symbol = ''
new_str = ''
count = 0
for s in my_str:

    if symbol != s:
        if len(symbol) > 0:
            new_str += f'{symbol}{count}'
            count = 0
        symbol = s
    count += 1 

if len(symbol) > 0:
    new_str += f'{symbol}{count}'       

print(new_str)            

new_str2 = ''
my_str = ''
my_num = ''
for s in new_str:
    if not s.isdigit():
        if len(my_str) > 0 and len(my_num) > 0:
            new_str2 += my_str * int(my_num)
            my_str = ''
            my_num = ''
        my_str += s
    else:
        my_num += s

if len(my_str) > 0 and len(my_num) > 0:
    new_str2 += my_str * int(my_num)

print(new_str2)
