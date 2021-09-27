# -*- coding: utf-8 -*-

def hourDegree():
    hours = int(input("Количество часов с начала суток(меньше 12) - "))
    minutes = int(input("Количество минут(меньше 60) - "))
    seconds = int(input("Количество секунд(меньше 60) - "))

    if((0 <= hours <= 12) and (0 <= minutes <= 60) and (0 <= seconds <= 60)):
        hourDegree = hours * 30 + minutes * 0.5 + seconds * (0.5 / 60)
        lastHourMinuteDegree = minutes * 6
        return hourDegree
    else:
        return "Некорректный ввод"

def minuteDegree():

    hoursDegree = float(input("На сколько градусов повернулась часовая стрелка - "))
    minuteDegree = hoursDegree % 30 * 12
    return minuteDegree

def reverseHourDegree():
    hoursDegree = float(input("На сколько градусов повернулась часовая стрелка - "))

    hoursTime = hoursDegree // 30 % 24
    minutesContainer = hoursDegree % 30 * 2
    minutesTime, secondsTime = divmod(minutesContainer, 1)

    print(hoursTime)
    print(minutesTime)
    print(secondsTime * 60)
    return "Операция проведена успешно"

print(hourDegree())
print(minuteDegree())
print(reverseHourDegree())