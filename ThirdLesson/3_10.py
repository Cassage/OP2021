# -*- coding: utf-8 -*-

def fiboSumWithK():
    N = int(input("Введите количество чисел - "))
    K = int(input("Введите порядковый номер - "))
    firstNumber = 0
    secondNumber = 1
    sum = 0
    for i in range(2, N):
        container = secondNumber
        secondNumber = firstNumber + secondNumber
        firstNumber = container
        if(i >= K - 1 ):
            print(secondNumber)
            sum += secondNumber
    print("Ответ:")
    return sum
print(fiboSumWithK())