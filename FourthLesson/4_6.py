# -*- coding: utf-8 -*-

def countF2():
    exampleString = input("Введите строку - ")
    if(exampleString.count("f") == 1):
        return -1
    if(exampleString.count("f") == 0):
        return - 2
    firstAppearance = exampleString.find("f")
    print("Ответ:")
    return exampleString.find("f", firstAppearance + 1)

print(countF2())