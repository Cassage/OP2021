# -*- coding: utf-8 -*-

def ladder():
    n = int(input("Введите число от 1 до 9 - "))
    if(1 < n <= 9):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, sep='', end='')
            print()
    else: return "Некорректный ввод"
    return "Конец лесенки"

print(ladder())