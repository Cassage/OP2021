# -*- coding: utf-8 -*-

def changeWords():
    exampleString = input("Введите строку - ")
    splitString = exampleString.split(" ")
    print("Ответ:")
    return splitString[1] + " " + splitString[0]
    
print(changeWords())
