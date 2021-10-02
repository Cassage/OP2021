# -*- coding: utf-8 -*-

def iterateAB():
    A = int(input("Первое число - "))
    B = int(input("Второе число - "))
    print("Вывод:")
    for i in range(A, B + 1):
        print(i)
    return "Конец цикла"

print(iterateAB())