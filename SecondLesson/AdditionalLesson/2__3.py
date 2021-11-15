# -*- coding: utf-8 -*-

def timeBetween():
    firstHours = int(input("Часы первого момента - "))
    firstMinutes = int(input("Минуты первого момента - "))
    firstSeconds = int(input("Секунды первого момента - "))

    secondHours = int(input("Часы второго момента - "))
    secondMinutes = int(input("Минуты второго момента - "))
    secondSeconds = int(input("Секунды второго момента - "))

    overallSeconds1 = firstHours * 3600 + firstMinutes * 60 + firstSeconds
    overallSeconds2 = secondHours * 3600 + secondMinutes * 60 + secondSeconds
    if(overallSeconds1 > overallSeconds2):
        return 3600 * 24 - (overallSeconds1 - overallSeconds2)
    else:
        return overallSeconds2 - overallSeconds1

print(timeBetween())  