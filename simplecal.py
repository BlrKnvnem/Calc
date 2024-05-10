from tkinter import *
from math import *

root = Tk()
root.title("Simple calculator")
e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def Button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def Button_clear():
    e.delete(0, END)

def Button_Bksp():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)

def Button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def Button_equal():
    second_number = e.get()
    if math == "addition":
        e.delete(0, END)
        e.insert(0, f_num + int(second_number))
    elif math == "Subtraction":
        e.delete(0, END)
        e.insert(0, f_num - int(second_number))
    elif math == "Multiplication":
        e.delete(0, END)
        e.insert(0, f_num * int(second_number))
    elif math == "Division":
        e.delete(0, END)
        e.insert(0, f_num / int(second_number))

def Button_Subtract():
    first_number = e.get()
    global f_num
    global math
    math = "Subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def Button_Multiply():
    first_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def Button_Divide():
    first_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = int(first_number)
    e.delete(0, END)

def Button_Tan():
    current_number = e.get()
    e.delete(0, END)
    e.insert(0, tan(float(current_number)))

def Button_cos():
    current_number=e.get()
    e.delete(0, END)
    e.insert(0, cos(float(current_number)))

def Button_sin():
    current_number=e.get()
    e.delete(0,END)
    e.insert(0,sin(float(current_number)))

Button_1 = Button(root, text=1, padx=40, pady=20, command=lambda: Button_click(1))
Button_2 = Button(root, text=2, padx=40, pady=20, command=lambda: Button_click(2))
Button_3 = Button(root, text=3, padx=40, pady=20, command=lambda: Button_click(3))
Button_4 = Button(root, text=4, padx=40, pady=20, command=lambda: Button_click(4))
Button_5 = Button(root, text=5, padx=40, pady=20, command=lambda: Button_click(5))
Button_6 = Button(root, text=6, padx=40, pady=20, command=lambda: Button_click(6))
Button_7 = Button(root, text=7, padx=40, pady=20, command=lambda: Button_click(7))
Button_8 = Button(root, text=8, padx=40, pady=20, command=lambda: Button_click(8))
Button_9 = Button(root, text=9, padx=40, pady=20, command=lambda: Button_click(9))
Button_0 = Button(root, text=0, padx=40, pady=20, command=lambda: Button_click(0))
Button_add = Button(root, text="+", padx=39, pady=20, command=Button_add)
Button_equal = Button(root, text="=", padx=37, pady=20, command=Button_equal)
Button_clear = Button(root, text="clear", padx=37, pady=20, command=Button_clear)
Button_Bksp = Button(root, text="bkps", padx=39, pady=20, command=Button_Bksp)
Button_Subtract = Button(root, text="-", padx=39, pady=20, command=Button_Subtract)
Button_Multiply = Button(root, text="*", padx=40, pady=20, command=Button_Multiply)
Button_Divide = Button(root, text="/", padx=41, pady=20, command=Button_Divide)
Button_Tan = Button(root, text="tan", padx=37, pady=20, command=Button_Tan)
Button_cos = Button(root, text="cos", padx=37, pady=20, command=Button_cos)
Button_sin = Button(root, text="sin", padx=37, pady=20, command=Button_sin)
Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)
Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)
Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)
Button_0.grid(row=4, column=1)
Button_add.grid(row=4, column=0)
Button_equal.grid(row=5, column=0)
Button_clear.grid(row=4, column=2)
Button_Bksp.grid(row=5, column=2)
Button_Subtract.grid(row=6, column=0)
Button_Multiply.grid(row=5, column=1)
Button_Divide.grid(row=6, column=2)
Button_Tan.grid(row=7, column=0)
Button_cos.grid(row=6, column=1)
Button_sin.grid(row=7, column=1)



root.mainloop()
