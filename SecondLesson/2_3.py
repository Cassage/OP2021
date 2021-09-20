# -*- coding: utf-8 -*-

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