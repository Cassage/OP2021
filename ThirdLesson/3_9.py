# -*- coding: utf-8 -*-

def fiboSum():
    N = int(input("Введите количество чисел - "))
    firstNumber = 0
    secondNumber = 1
    sum = 1
    for i in range(2, N):
        container = secondNumber
        secondNumber = firstNumber + secondNumber
        firstNumber = container
        sum += secondNumber
    print("Ответ:")
    return sum

print(fiboSum())

