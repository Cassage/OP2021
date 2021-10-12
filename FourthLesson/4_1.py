# -*- coding: utf-8 -*-
def stringOperations():
    exampleString = input("Введите строку - ")
    iString = exampleString[2]
    iiString = exampleString[len(exampleString) - 2]
    iiiString = exampleString[0:5]
    ivString = exampleString[0:len(exampleString) - 3]
    vString = exampleString[0::2]
    viString = exampleString[1::2]
    viiString = exampleString[::-1]
    viiiString = viiString[::-2]
    ixString = len(exampleString)
    print(iString)
    print(iiString)
    print(iiiString)
    print(ivString)
    print(vString)
    print(viString)
    print(viiString)
    print(viiiString)
    print(ixString)
    print("\n")
    return "Конец"

print(stringOperations())
