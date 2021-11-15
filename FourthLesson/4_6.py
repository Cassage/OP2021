# -*- coding: utf-8 -*-

def countF2():
    exampleString = input("Введите строку - ")
    if(exampleString.count("f") == 1):
        print(-1)
    if(exampleString.count("f") == 0):
        print(-2)
    firstAppearance = exampleString.find("f")
    print("Ответ:")
    print(exampleString.find("f", firstAppearance + 1))

countF2()