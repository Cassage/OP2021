# -*- coding: utf-8 -*-

def splitString():
    exampleString = input("Введите строку - ")
    firstPartSize = len(exampleString) // 2 + len(exampleString) % 2
    firstPart = exampleString[0:firstPartSize]
    secondPart = exampleString[firstPartSize:]
    print("Ответ:")
    print(secondPart + firstPart)
splitString()