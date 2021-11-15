# -*- coding: utf-8 -*-

def deleteBetween():
    exampleString = input("Введите строку - ")
    firstAppearance = exampleString.find("h")
    lastAppearance = exampleString.rfind("h")
    print("Ответ:")
    print(exampleString[0:firstAppearance] + exampleString[lastAppearance + 1:])
deleteBetween()