# -*- coding: utf-8 -*-

def iterateAB():
    A = int(input("Первое число - "))
    B = int(input("Второе число - "))
    print("Вывод:")
    for i in range(A, B - 1, -1):
        if(i % 2 != 0):
            print(i)
    return "Конец цикла"

print(iterateAB())