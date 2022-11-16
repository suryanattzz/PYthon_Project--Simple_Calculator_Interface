from tkinter import *

# simple calculator
cal = Tk()
cal.title("SIMPLE CALCULATOR")

e = Entry(cal, width=60, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def func(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def func_clr():
    e.delete(0, END)


def result():
    a = e.get()
    a = eval(a)
    func_clr()
    e.insert("end", a)


button1 = Button(cal, text="1", padx=40, pady=40, borderwidth=10, command=lambda: func(1))
button2 = Button(cal, text="2", padx=40, pady=40, borderwidth=10, command=lambda: func(2))
button3 = Button(cal, text="3", padx=40, pady=40, borderwidth=10, command=lambda: func(3))
button4 = Button(cal, text="4", padx=40, pady=40, borderwidth=10, command=lambda: func(4))
button5 = Button(cal, text="5", padx=40, pady=40, borderwidth=10, command=lambda: func(5))
button6 = Button(cal, text="6", padx=40, pady=40, borderwidth=10, command=lambda: func(6))
button7 = Button(cal, text="7", padx=40, pady=40, borderwidth=10, command=lambda: func(7))
button8 = Button(cal, text="8", padx=40, pady=40, borderwidth=10, command=lambda: func(8))
button9 = Button(cal, text="9", padx=40, pady=40, borderwidth=10, command=lambda: func(9))
button0 = Button(cal, text="0", padx=40, pady=40, borderwidth=10, command=lambda: func(0))
button00 = Button(cal, text="00", padx=40, pady="40", borderwidth=10, command=lambda: e.insert("end", "00"))

button_add = Button(cal, text="+", padx=80, pady=40, borderwidth=15, command=lambda: e.insert("end", "+"))
button_sub = Button(cal, text="-", padx=80, pady=40, borderwidth=15, command=lambda: e.insert("end", "-"))
button_mul = Button(cal, text="*", padx=80, pady=40, borderwidth=15, command=lambda: e.insert("end", "*"))
button_div = Button(cal, text="/", padx=80, pady=40, borderwidth=15, command=lambda: e.insert("end", "/"))

button_equal = Button(cal, text="=", padx=40, pady=40, borderwidth=15, bg="black", fg="white", command=result)
button_clear = Button(cal, text="clear", padx=40, pady=40, borderwidth=15, command=func_clr)

# button packing
button1.grid(row="1", column="0")
button2.grid(row="1", column="1")
button3.grid(row="1", column="2")

button4.grid(row="2", column="0")
button5.grid(row="2", column="1")
button6.grid(row="2", column="2")

button7.grid(row="3", column="0")
button8.grid(row="3", column="1")
button9.grid(row="3", column="2")

button0.grid(row="4", column="0")
button00.grid(row="4", column="1")

button_add.grid(row="1 ", column="3")
button_sub.grid(row="2 ", column="3")
button_mul.grid(row="3", column="3")
button_div.grid(row="4", column="3")
button_equal.grid(row="4", column="2")
button_clear.grid(row="0", column="3")

cal.mainloop()