# -*- coding: utf-8 -*-

# Третье задание
print("Третье задание: ")

def enrollmentCheck(age, name):
    if(age > 0 and age < 75 and name != "Иван"):
        if age >= 16:
            return("Поздравляем вы поступили в ВГУИТ")
        else:
            print("Сначала нужно окончить школу")
            return("Осталось учиться лет: " + str(16-age))
    else:
        return "Некорректный ввод"
        

print(enrollmentCheck(-1, "Влад"))
print(enrollmentCheck(16, "Саша"))
print(enrollmentCheck(16, "Иван"))
print(enrollmentCheck(13, "Дима"))