from tkinter import *


# Button click causes a trigger
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# Clear expression
def btn_clear():
    global expression
    expression = ""
    input_text.set("")


# Clear input entry
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


# Root
root = Tk()
root.geometry("312x324")
root.resizable(width=False, height=False)
root.title("CALCULATOR")

# Input expression
expression = ""
input_text = StringVar()

# Input frame
input_frame = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1)
input_frame.pack(side=TOP)

# Input entry
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame for buttons
btns_frame = Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# Clear button
clear = Button(btns_frame, text="Clear", fg="black", width=32, height=3, bd=0, bg="orange", cursor="hand2",
               command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

# Division
divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="orange", cursor="hand2",
       command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

# 7
seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
               command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

# 8
eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
               command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

# 9
nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
              command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

# Multiplication
multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="orange", cursor="hand2",
                  command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

# 4
four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
              command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

# 5
five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
              command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

# 6
six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
             command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

# Subtraction
minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="orange", cursor="hand2",
               command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

# 1
one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
             command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

# 2
two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
             command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

# 3
three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="yellow", cursor="hand2",
               command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

# Addition
plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="orange", cursor="hand2",
              command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

# 0
zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="yellow", cursor="hand2",
       command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

# Decimal point
point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="orange", cursor="hand2",
               command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

# Equal to answer
equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="orange", cursor="hand2",
                command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()
