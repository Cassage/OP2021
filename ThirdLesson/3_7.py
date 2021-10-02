# -*- coding: utf-8 -*-

n = int(input("Введите число - "))

def factorialSum(n, overallSum):
    x = n
    overallSum = overallSum
    sum = 1
    for i in range(1, x + 1):
        sum *= i 
    if(x != 1):
        overallSum += sum
        return factorialSum(x - 1, overallSum)
    else:
        print("Ответ")
        return overallSum
    
    

print(factorialSum(n, 1))