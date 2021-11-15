# -*- coding: utf-8 -*-

# Четвёртое задание
print("Четвёртое задание: ")


def time(seconds):
    fullTime = str(seconds // 86400) + ":" + str(seconds % 86400 // 3600) + ":" + str(seconds % 3600 // 60) + ":" + str(seconds % 3600 % 60)
    return fullTime
print(time(5000))
print(time(90000))