# -*- coding: utf-8 -*-

def slimeTime():
    height = int(input("Высота шеста - "))
    slimeGain = int(input("На сколько поднимается - "))
    slimeLose = int(input("На сколько опускается - "))

    daysCounter = 1
    moveCounter = 0

    while(True):
        moveCounter += slimeGain
        if(moveCounter > height):
            break
        else:
            moveCounter -= slimeLose
            daysCounter += 1
    
    return daysCounter

print(slimeTime())