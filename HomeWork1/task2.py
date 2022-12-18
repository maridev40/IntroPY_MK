# Задача 2
# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in True, False:
    for y in True, False:
        for z in True, False:
            print(f'x = {x} y = {y} z = {z}', end=' -> ') 
            print(not (x or y or z) == (not x and not y and not z))