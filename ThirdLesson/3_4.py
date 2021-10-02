# -*- coding: utf-8 -*-

def sumN():
    sum = 0
    for i in range(int(input("Введите количество чисел - "))):
        sum += int(input("Введите число - "))
    print("Ответ:")
    return sum

print(sumN())