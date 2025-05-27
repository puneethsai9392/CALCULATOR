from tkinter import *

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def close_app():
    gui.destroy()

def key_press(event):
    global expression
    if event.char.isdigit() or event.char in "+-*/.":
        expression += event.char
        equation.set(expression)
    elif event.keysym == "Return":
        equalpress()
    elif event.keysym == "BackSpace":
        backspace()

def handle_button(text):
    expression_field.focus_set()  # Refocus so keyboard keeps working
    if text == "Clear":
        clear()
    elif text == "Backspace":
        backspace()
    elif text == "=":
        equalpress()
    elif text == "Quit":
        close_app()
    else:
        press(text)

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="green")
    gui.title("Enhanced Calculator")
    gui.geometry("400x350")

    equation = StringVar()

    # Entry field
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 20), bd=5, relief="ridge", justify="right")
    expression_field.grid(columnspan=4, ipadx=90, pady=10)
    expression_field.focus_set()  # Set initial focus to enable keyboard input

    # Button layout
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('Clear', 5, 0), ('Backspace', 5, 1), ('Quit', 5, 2)
    ]

    # Bind keyboard input
    gui.bind("<Key>", key_press)

    # Create buttons
    for (text, row, col) in buttons:
        Button(gui, text=text, fg="black", bg="white", font=("Arial", 15),
               command=lambda t=text: handle_button(t),
               height=2, width=10).grid(row=row, column=col, padx=5, pady=5)

    gui.mainloop()
