# -*- coding: utf-8 -*-

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