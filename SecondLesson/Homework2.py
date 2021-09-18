# -*- coding: utf-8 -*-

# Первое задание
def sumOfThree():
    print("Введите входные данные (3 числа)")
    x = int(input())
    y = int(input())
    z = int(input())
    print("Ответ:")
    sum = x + y + z
    return sum

print("\n")
print("Первое задание: ")
print(sumOfThree())
print("\n")

# Второе задание
def areaOfTriangle():
    print("Введите входные данные (2 числа)")
    firstSide = int(input("Длина первой стороны - "))
    secondSide = int(input("Длина второй стороны - "))
    print("Ответ:")
    return firstSide * secondSide * 0.5

print("Второе задание: ")
print(areaOfTriangle())
print("\n")

# Третье задание
def timeSinceStart():
    print("Введите входные данные (1 число)")
    time = int(input("Количество минут - "))
    print("Ответ:")
    hours = time // 60
    minutes = time % 60
    return "time - " + str(hours % 24) + ":" + str(minutes)

print("Третье задание: ")
print(timeSinceStart())
print("\n")

# Четвёртое задание
def lengthOfLace():
    print("Введите входные данные (4 числа)")
    a = int(input("Расстояние между рядами - "))
    b = int(input("Расстояние между отверстиями в ряду - "))
    l = int(input("Длина свободного конца шнурка - "))
    N = int(input("Кол-во отверстий в ряду - "))
    print("Ответ:")
    return (2 * N - 1) * a + 2 * l + 2 * (N - 1) * b

print("Четвёртое задание: ")
print(lengthOfLace())
print("\n")

# Пятое задание
def minOuttaThree():
    print("Введите входные данные (3 числа)")
    x = int(input())
    y = int(input())
    z = int(input())
    print("Ответ:")
    return min(x,y,z)

print("Пятое задание: ")
print(minOuttaThree())
print("\n")

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

# Седьмое задание
def isLeapYear():
    print("Введите входные данные (1 число)")
    year = int(input("Год  - "))
    print("Ответ:")
    if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return "Да"
    else:
        return "Нет"

print("Седьмое задание: ")
print(isLeapYear())
print("\n")

# Восьмое задание
def isTheSameNumber():
    print("Введите входные данные (3 числа)")
    x = int(input())
    y = int(input())
    z = int(input())
    print("Ответ:")
    if(x == y == z):
        return 3
    elif(x == y or z == y or x == z):
        return 2
    else:
        return 0

print("Восьмое задание: ")
print(isTheSameNumber())
print("\n")
# Девятое задание
def isPossibleToGetKPart():
    print("Введите входные данные (3 числа)")
    n = int(input())
    m = int(input())
    k = int(input())
    print("Ответ:")
    if(n * m > k and (k % m == 0 or k % n == 0)):
        return "Да"
    else:
        return "Нет"

print("Девятое задание: ")
print("\n")
print(isPossibleToGetKPart())



# Готовая работа



