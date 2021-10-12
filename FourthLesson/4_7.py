# -*- coding: utf-8 -*-

def deleteBetween():
    exampleString = input("Введите строку - ")
    firstAppearance = exampleString.find("h")
    lastAppearance = exampleString.rfind("h")
    print("Ответ:")
    return exampleString[0:firstAppearance] + exampleString[lastAppearance + 1:]
print(deleteBetween())