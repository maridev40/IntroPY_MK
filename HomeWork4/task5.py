# Задача 5
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

import re

def getPolyn(paht):
    my_dict = {}
    with open(paht, 'r') as data:
        for line in data:
            my_str = re.findall('\+* *\d+\**x\**\**\d*', line)
            for el in my_str:
                my_int = int(re.findall('^\+* *\d+', el)[0].replace(' ', ''))
                if el[len(el) - 1].isdigit():
                    my_dict[int(el[len(el) - 1])] = my_int
                else:
                    my_dict[1] = my_int 
            my_str = re.findall(' \+ \d+ = 0', line)
            my_int = int(re.findall(' \+* *\d+', my_str[0])[0].replace(' ', ''))
            my_dict[0] = my_int
    
    return my_dict

def getSumPolyn(polyn1, polyn2):
    pol_return = {}
    if len(polyn1) > len(polyn2):
        for p in polyn1:
            pol_return[p] = polyn1[p]
        for p in polyn2:
            pol_return[p] += polyn2[p]  
    else:
        for p in polyn2:
            pol_return[p] = polyn2[p]  
        for p in polyn1:
            pol_return[p] += polyn1[p]    
   
    return pol_return

def setPolyn(polyn, path):
    pol_str = ''
    for i in polyn:
        if len(pol_str) > 0:
            pol_str += ' + '
        if i == 0:
            pol_str += str(polyn[i]) + ' = 0'
        else:
            pol_str += str(polyn[i]) + '*x**' + str(i)
    
    with open(path, 'w') as data:
        data.write(pol_str)


my_dict1 = getPolyn('file1.txt')  
print(f'file1 -> {my_dict1}')      
my_dict2 = getPolyn('file2.txt')  
print(f'file2 -> {my_dict2}')     

my_dict = getSumPolyn(my_dict1, my_dict2)
print(f'сумма -> {my_dict}') 

setPolyn(my_dict, 'file_sum.txt')
