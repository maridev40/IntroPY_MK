# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

my_str = 'WWWfffffhhhhhhhh rrrrrrDDDDDsss'
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
index = 0
for s in new_str:
    index += 1
    if index % 2 == 0:
        new_str2 += new_str[index - 2] * int(new_str[index - 1])

print(new_str2)
