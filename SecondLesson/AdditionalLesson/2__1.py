# -*- coding: utf-8 -*-

def lastNumber():
    number = input("Введите число - ")
    checker = "123456789"
    if(number[-1] in checker):
        return number[-1]
    else:
        return "Неправильный ввод"
print(lastNumber())