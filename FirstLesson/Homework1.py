# -*- coding: utf-8 -*-

# Первое задание
print("Первое задание: Курс Основы программирования начался")

OstatokDelenia = 16823 * 12302 % 3092

# Второе задание
print("Второе задание: " + str(OstatokDelenia))

# Третье задание
print("Третье задание: ")

def enrollmentCheck(age, name):
    if(age > 0 and age < 75):
        if(name == "Иван"):
            print("Вас зовут Иван")
        if age >= 16:
            print("Поздравляем вы поступили в ВГУИТ")
        else:
            print("Сначала нужно окончить школу")
            print("Осталось учиться лет: " + str(16-age))
    else:
        print("Некорректный ввод")
    return("Работает нормально")
        

print(enrollmentCheck(-1, "Влад"))
print(enrollmentCheck(16, "Иван"))
print(enrollmentCheck(13, "Дима"))

# Четвёртое задание
print("Четвёртое задание: ")

seconds = 5000
time = str(seconds // 3600) + ":" + str(seconds % 3600 // 60) + ":" + str(seconds % 3600 % 60)
print(time)

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
        print("Это число чётное")
    else:
        print("Это число нечётное")

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

