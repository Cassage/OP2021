# -*- coding: utf-8 -*-

def changeWords():
    exampleString = input("Введите строку - ")
    splitString = exampleString.split(" ")
    print("Ответ:")
    print(splitString[1] + " " + splitString[0])
    
changeWords()
