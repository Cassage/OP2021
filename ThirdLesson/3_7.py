# -*- coding: utf-8 -*-

n = int(input("Введите число - "))

def factorialSum(n):
    x = n
    fact = 1
    sum = 0
    for i in range(1, x + 1):
        fact = fact * i
        sum = sum + fact
    
    else:
        print("Ответ:")
        return sum
    
    
print(factorialSum(n))