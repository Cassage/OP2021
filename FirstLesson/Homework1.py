# -*- coding: utf-8 -*-

# Первое задание
print("Первое задание: Курс Основы программирования начался")

OstatokDelenia = 16823 * 12302 % 3092

# Второе задание
print("Второе задание: " + str(OstatokDelenia))

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

# Четвёртое задание
print("Четвёртое задание: ")


def time(seconds):
    fullTime = str(seconds // 86400) + ":" + str(seconds % 86400 // 3600) + ":" + str(seconds % 3600 // 60) + ":" + str(seconds % 3600 % 60)
    return fullTime
print(time(5000))
print(time(90000))

# Пятое задание
print("Пятое задание: ")

n = 10
StringN = n + n ** 2 + n ** 3 + n ** 4 + n ** 5
print(StringN)

# Шестое задание
print("Шестое задание: ")

x = 5
y = 6
print(x, y)
x, y = y, x
print(x, y)

# Седьмое задание
print("Седьмое задание:")

def isEven(number):
    if(number % 2 == 0):
        return("Это число чётное")
    else:
        return("Это число нечётное")
   

print(isEven(4))
print(isEven(5))

# Допольнительное задание (Найти первые десять натуральных чисел)
print("Доп. задание: ")

realCounter = 0
for x in range(1, 1000):
    counter = 0
    for y in range(1, 1000):
        if(x % y == 0):
            counter += 1
    if(counter == 2):
        realCounter += 1
        print(x)
    if(realCounter == 10):
        break

