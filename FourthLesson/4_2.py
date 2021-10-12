# -*- coding: utf-8 -*-

def countWords():
    exampleString = input("Введите строку - ")
    print("Ответ:")
    return exampleString.count(" ") + 1

print(countWords())