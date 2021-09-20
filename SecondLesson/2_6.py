# -*- coding: utf-8 -*-

# Шестое задание
def isTheSameColor():
    print("Введите входные данные (4 числа)")
    firstX = int(input("Номер столбца первой клетки - "))
    firstY = int(input("Номер строки первой клетки - "))
    secondX = int(input("Номер столбца второй клетки - "))
    secondY = int(input("Номер строки второй клетки - "))
    print("Ответ:")
    if(1 <= firstX <= 8 and 1 <= firstY <= 8 and 1 <= secondX <= 8 and 1 <= secondY <= 8):
        if((firstY % 2 != 0 and firstX % 2 != 0) or (firstY % 2 == 0 and firstX % 2 == 0)):
            firstColor = "Чёрный"
        else:
            secondColor = "Белый"
        if((secondY % 2 != 0 and secondX % 2 != 0) or (secondY % 2 == 0 and secondX % 2 == 0)):
            secondColor = "Чёрный"
        else:
            secondColor = "Белый"
        if(secondColor == firstColor):
            return "Да"
        else:
            return "Нет"
    else:
        return "Некорректный ввод"

print("Шестое задание задание: ")
print(isTheSameColor())
print("\n")