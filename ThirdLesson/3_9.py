# -*- coding: utf-8 -*-

def fiboSum():
    N = int(input("Введите количество чисел - "))
    fiboArr = [0, 1]
    for i in range(2, N):
        fiboFirst = fiboArr[i - 1]
        fiboSecond = fiboArr[i - 2]
        fiboArr.append(fiboFirst + fiboSecond)
    print("Ответ:")
    return sum(fiboArr)

print(fiboSum())

