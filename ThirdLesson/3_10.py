# -*- coding: utf-8 -*-

def fiboSumWithK():
    N = int(input("Введите количество чисел - "))
    K = int(input("Введите порядковый номер - "))
    fiboArr = [0, 1]
    for i in range(2, N + K):
        fiboFirst = fiboArr[i - 1]
        fiboSecond = fiboArr[i - 2]
        fiboArr.append(fiboFirst + fiboSecond)
    print("Ответ:")
    print(fiboArr)
    return sum(fiboArr[K - 1:])

print(fiboSumWithK())