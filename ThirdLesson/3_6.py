# -*- coding: utf-8 -*-

def factorial():
    n = int(input("Введите число - "))
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    print("Ответ")
    return sum

print(factorial())