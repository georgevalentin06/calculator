from tkinter import *

window = Tk()
window.title("Calculator")
window.maxsize(230,200)
window.minsize(230,200)


calculation = ""

def press_key(num):
    global calculation
    calculation = ""
    calculation += str(num)
    result.insert(END, calculation)

def clear():
    result.delete(0, 'end')

def add_symbol(symbol):
    equation = result.get()
    if equation[-1].isdigit():
        result.insert(END, symbol)

def equal():
    try:
        equation = result.get()
        clear()
        result.insert(END, eval(equation))
    except SyntaxError:
        result.insert(END, equation)


result = Entry(borderwidth=3, font=('default, 14'))
result.grid(row=0, column=0, columnspan=4, ipady=3 )

btn_1 = Button(text="1", width=5, height=2, command=lambda:press_key(1))
btn_1.grid(row=3, column=0,sticky="nsew")

btn_2 = Button(text="2", width=5, height=2,command=lambda:press_key(2))
btn_2.grid(row=3, column=1,sticky="nsew")

btn_3 = Button(text="3", width=5, height=2, command=lambda:press_key(3))
btn_3.grid(row=3, column=2,sticky="nsew")

btn_4 = Button(text="4", width=5, height=2, command=lambda:press_key(4))
btn_4.grid(row=2, column=0,sticky="nsew")

btn_5 = Button(text="5", width=5, height=2, command=lambda:press_key(5))
btn_5.grid(row=2, column=1, sticky="nsew")

btn_6 = Button(text="6", width=5, height=2, command=lambda:press_key(6))
btn_6.grid(row=2, column=2, sticky="nsew")

btn_7 = Button(text="7", width=5, height=2, command=lambda:press_key(7))
btn_7.grid(row=1, column=0, sticky="nsew")

btn_8 = Button(text="8", width=5, height=2, command=lambda:press_key(8))
btn_8.grid(row=1, column=1, sticky="nsew")

btn_9 = Button(text="9", width=5, height=2, command=lambda:press_key(9))
btn_9.grid(row=1, column=2, sticky="nsew")

btn_0 = Button(text="0", width=5, height=2, command=lambda:press_key(0))
btn_0.grid(row=4, column=0, sticky="nsew")

btn_c = Button(text="C", width=5, height=2, command=clear)
btn_c.grid(row=4, column=2, sticky="nsew")

btn_add = Button(text="+", width=5, height=2, command=lambda:add_symbol("+"))
btn_add.grid(row=1, column=3, sticky="nsew")

btn_minus = Button(text="-", width=5, height=2,command=lambda:add_symbol("-"))
btn_minus.grid(row=2, column=3, sticky="nsew")

btn_multiply = Button(text="*", width=5, height=2, command=lambda:add_symbol("*"))
btn_multiply.grid(row=3, column=3, sticky="nsew")

btn_divide = Button(text="/", width=5, height=2, command=lambda:add_symbol("/"))
btn_divide.grid(row=4, column=3, sticky="nsew")

btn_equal = Button(text="=", width=5, height=2, command=equal)
btn_equal.grid(row=4, column=1, sticky="nsew")


window.mainloop()