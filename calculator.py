
# import tkinter
import tkinter
from tkinter import *

# Set window width,height,title,background color and disable resizable property
window = Tk()
window.geometry("300x400")
window.title("CASIO")
window.configure(bg='black')
window.resizable(False, False)


# To set the input field
display = StringVar()
input_text = Entry(window, textvariable=display, width=20, bd=18, state="disabled", font=25, justify="right")
input_text.place(x=18, y=20)


# Function for clearing the screen
def clear():
    display.set("")


# Function for displaying user entered value on screen
def print_input(key):
    if display.get() == "ERROR":
        clear()
    inp = display.get() + key
    display.set(inp)


def print_operator(op):
    # Check errors
    try:
        inp = eval(display.get())
        display.set(inp)
    except:
        inp = "ERROR"
        display.set(inp)


# Clear button
button_clear = Button(text="Clear", width=7, height=2, bg="green", command=clear)


# Button 7,8,9,-
button7 = Button(text="7", width=4, height=2, bg="gray", command=lambda: print_input("7"))
button8 = Button(text="8", width=4, height=2, bg="gray", command=lambda: print_input("8"))
button9 = Button(text="9", width=4, height=2, bg="gray", command=lambda: print_input("9"))
button_div = Button(text="/", width=7, height=2, bg="white", command=lambda: print_input("/"))


# Button 4,5,6,*
button4 = Button(text="4", width=4, height=2, bg="gray", command=lambda: print_input("4"))
button5 = Button(text="5", width=4, height=2, bg="gray", command=lambda: print_input("5"))
button6 = Button(text="6", width=4, height=2, bg="gray", command=lambda: print_input("6"))
button_mul = Button(text="*", width=7, height=2, bg="white", command=lambda: print_input("*"))

# Button 1,2,3,-
button1 = Button(text="1", width=4, height=2, bg="gray", command=lambda: print_input("1"))
button2 = Button(text="2", width=4, height=2, bg="gray", command=lambda: print_input("2"))
button3 = Button(text="3", width=4, height=2, bg="gray", command=lambda: print_input("3"))
button_min = Button(text="-", width=7, height=2, bg="white", command=lambda: print_input("-"))

# Button .,0,=,+
button_dot = Button(text=".", width=4, height=2, bg="white", command=lambda: print_input("."))
button0 = Button(text="0", width=4, height=2, bg="gray", command=lambda: print_input("0"))
button_equal = Button(text="=", width=4, height=2, bg="white", command=lambda: print_operator("="))
button_add = Button(text="+", width=7, height=2, bg="white", command=lambda: print_input("+"))

# To align buttons
button_clear.place(x=220, y=90)

button7.place(x=40, y=140)
button8.place(x=100, y=140)
button9.place(x=160, y=140)
button_div.place(x=220, y=140)

button4.place(x=40, y=200)
button5.place(x=100, y=200)
button6.place(x=160, y=200)
button_mul.place(x=220, y=200)

button1.place(x=40, y=260)
button2.place(x=100, y=260)
button3.place(x=160, y=260)
button_min.place(x=220, y=260)

button_dot.place(x=40, y=320)
button0.place(x=100, y=320)
button_equal.place(x=160, y=320)
button_add.place(x=220, y=320)


window.mainloop()
