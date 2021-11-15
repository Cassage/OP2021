# -*- coding: utf-8 -*-

def deleteFromString():
    exampleString = input("Введите строку - ")
    symbolToDelete = input("Введите символ для замены - ")
    print(exampleString.replace(symbolToDelete, ""))
deleteFromString()