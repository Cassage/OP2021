# -*- coding: utf-8 -*-

def countF():
    exampleString = input("Введите строку - ")
    if(exampleString.count("f") == 0):
        return
    if(exampleString.count("f") == 1):
        print("Ответ:")
        print(exampleString.find("f"))
    else:
        print("Ответ:")
        print("Первое появление - " + str(exampleString.find("f")))
        print("Последнее появление - " + str(exampleString.rfind("f")))

    
countF()