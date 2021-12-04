# -*- coding: utf-8 -*-

from tkinter import *

def squareUp():
    arg = txt.get()
    i = 1
    N = int(arg)
    result = ""
    while i * i <= N:
        i+=1
        result += str(i)
    resultlbl_2.configure(text = result)

def findDel():
    arg = txt1.get()
    i = 2
    N = int(arg)
    while N % i != 0:
        i += 1
    resultlbl1_2.configure(text = i)

def powFinder():
    arg = txt2.get()
    i = 2
    powContainer = 2
    counter = 1
    N = int(arg)

    while powContainer * i < N:
        powContainer *= i
        counter+=1
    result = "cтепень: " + str(powContainer) + " " + "показатель степени: " + str(counter) 
    resultlbl2_2.configure(text = result)

def sport():
    x = int(txt3_1.get())
    y = int(txt3_2.get())
    counter = 1
    while x < y:
        x *= 1.1
        counter+=1
    resultlbl3_2.configure(text = counter)

until0Counter1 = 0
def until0():
    global until0Counter1
    arg = txt4.get()
    print(arg)
    if(arg != "0"):
        until0Counter1 += 1
        print(until0Counter1)
    else:
        resultlbl4_2.configure(text = until0Counter1)
        until0Counter1 = 0
    txt4.delete(0, END)
    
until0Counter2 = 0
sum = 0
def until0Average():
    global until0Counter2
    arg = txt5.get()
    global sum
    if arg != "0":
        until0Counter2+=1
        sum += int(arg)
    else:
        resultlbl5_2.configure(text = sum / until0Counter2)
        until0Counter2 = 0
        sum = 0
    txt5.delete(0, END)

until0Counter3 = 0
container1 = 10000000
def until0Bigger():
    arg = txt6.get()
    global until0Counter3
    global container1
    if(int(arg) > container1):
        until0Counter3+=1
    container1= int(arg)
    if(arg == "0"):
        resultlbl6_2.configure(text = until0Counter3)
        container1 = 100000
        until0Counter3 = 0
    txt6.delete(0, END)

until0Counter4 = 0
container2 = 10000000
maxStreak = 0
def until0Streak():
    arg = txt7.get()
    global until0Counter4
    global container2
    global maxStreak
   
    x = int(arg)
    if(x == container2):
            until0Counter4 += 1
    else:
        if(maxStreak < until0Counter4):
            maxStreak = until0Counter4
        until0Counter4 = 1
    container2 = x
    if(x == 0):
        resultlbl7_2.configure(text = (max(maxStreak, until0Counter4)))
        container2 = 1000000
    txt7.delete(0, END)


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
lbl = Label(window, text = "Введите число")
lbl.grid(column=0, row = 0)
txt = Entry(window, width = 10)
txt.grid(column=1, row = 0)
btn = Button(window, text = "Выполнить фукнцию 5_2", command = squareUp)
btn.grid(column=2, row = 0)
resultlbl_1 = Label(window, text = "Результат: ")
resultlbl_1.grid(column = 3, row = 0)
resultlbl_2 = Label(window, text = "")
resultlbl_2.grid(column=4, row = 0)

lbl1 = Label(window, text = "Введите число")
lbl1.grid(column=0, row = 1)
txt1 = Entry(window, width = 10)
txt1.grid(column=1, row = 1)
btn1 = Button(window, text = "Выполнить функцию 5_2",command = findDel)
btn1.grid(column=2, row = 1)
resultlbl1_1 = Label(window, text = "Результат: ")
resultlbl1_1.grid(column = 3, row = 1)
resultlbl1_2 = Label(window, text = "")
resultlbl1_2.grid(column=4, row = 1)

lbl2 = Label(window, text = "Введите число")
lbl2.grid(column=0, row = 2)
txt2 = Entry(window, width = 10)
txt2.grid(column=1, row = 2)
btn2 = Button(window, text = "Выполнить функцию 5_3", command = powFinder)
btn2.grid(column=2, row = 2)
resultlbl2_1 = Label(window, text = "Результат: ")
resultlbl2_1.grid(column = 3, row = 2)
resultlbl2_2 = Label(window, text = "")
resultlbl2_2.grid(column=4, row = 2)

lbl3 = Label(window, text = "Введите 2 числа")
lbl3.grid(column=0, row = 3)
txt3_1 = Entry(window, width = 10)
txt3_1.grid(column=1, row = 3)
txt3_2 = Entry(window, width = 10)
txt3_2.grid(column=2, row = 3)
btn3 = Button(window, text = "Выполнить функцию 5_4", command=sport)
btn3.grid(column=3, row = 3)
resultlbl3_1 = Label(window, text = "Результат: ")
resultlbl3_1.grid(column = 4, row = 3)
resultlbl3_2 = Label(window, text = "")
resultlbl3_2.grid(column=5, row = 3)

lbl4_1 = Label(window, text = "Число 0 выведет результат")
lbl4_1.grid(column=0, row = 4)
txt4 = Entry(window, width = 10)
txt4.grid(column=1, row = 4)
btn4 = Button(window, text = "Выполнить функцию 5_5", command=until0)
btn4.grid(column=2, row = 4)
resultlbl4_1 = Label(window, text = "Результат: ")
resultlbl4_1.grid(column = 3, row = 4)
resultlbl4_2 = Label(window, text = "")
resultlbl4_2.grid(column=4, row = 4)


lbl5 = Label(window, text = "Число 0 выведет результат")
lbl5.grid(column=0, row = 5)
txt5 = Entry(window, width = 10)
txt5.grid(column=1, row = 5)
btn5 = Button(window, text = "Выполнить функцию 5_6", command=until0Average)
btn5.grid(column=2, row = 5)
resultlbl5_1 = Label(window, text = "Результат: ")
resultlbl5_1.grid(column = 3, row = 5)
resultlbl5_2 = Label(window, text = "")
resultlbl5_2.grid(column=4, row = 5)


lbl6 = Label(window, text = "Число 0 выведет результат")
lbl6.grid(column=0, row = 6)
txt6 = Entry(window, width = 10)
txt6.grid(column=1, row = 6)
btn6 = Button(window, text = "Выполнить функцию 5_7", command=until0Bigger)
btn6.grid(column=2, row = 6)
resultlbl6_1 = Label(window, text = "Результат: ")
resultlbl6_1.grid(column = 3, row = 6)
resultlbl6_2 = Label(window, text = "")
resultlbl6_2.grid(column=4, row = 6)

lbl7 = Label(window, text = "Число 0 выведет результат")
lbl7.grid(column=0, row = 7)
txt7 = Entry(window, width = 10)
txt7.grid(column=1, row = 7)
btn7 = Button(window, text = "Выполнить функцию 5_8", command=until0Streak)
btn7.grid(column=2, row = 7)
resultlbl7_1 = Label(window, text = "Результат: ")
resultlbl7_1.grid(column = 3, row = 7)
resultlbl7_2 = Label(window, text = "")
resultlbl7_2.grid(column=4, row = 7)



window.mainloop()