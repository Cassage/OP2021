# -*- coding: utf-8 -*-

def reverseBetween():
    exampleString = input("Введите строку - ")
    firstAppearance = exampleString.find("h")
    lastAppearance = exampleString.rfind("h")
    print("Ответ:")
    return exampleString[0:firstAppearance + 1] + exampleString[firstAppearance + 1:lastAppearance][::-1] + exampleString[lastAppearance:]
print(reverseBetween())