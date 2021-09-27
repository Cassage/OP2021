# -*- coding: utf-8 -*-

def floatPart():
    number = input("Введите число - ")
    floating = number.split(".")
    if(floating == "" or '.' not in number):
        return "Некорректный ввод"
    else:
        print("Первая цифра после десятичной точки - " + floating[-1][0])
        print("\n")
        return floating[-1]

print(floatPart())
