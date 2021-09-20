# -*- coding: utf-8 -*-

# Допольнительное задание (Найти первые десять натуральных чисел)
print("Доп. задание: ")

realCounter = 0
for x in range(1, 1000):
    counter = 0
    for y in range(1, 1000):
        if(x % y == 0):
            counter += 1
    if(counter == 2):
        realCounter += 1
        print(x)
    if(realCounter == 10):
        break