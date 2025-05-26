from tkinter import *
expression = ""
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))  # Evaluates the expression
        equation.set(total)
        expression = ""  # Clears expression after calculation
    except:
        equation.set("Error")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
def backspace():
    global expression
    expression = expression[:-1]  # Removes last character
    equation.set(expression)
def close_app():
    gui.destroy()
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="green")  # Set background color
    gui.title("Enhanced Calculator")
    gui.geometry("400x350")  # Increase window size
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 20), bd=5, relief="ridge", justify="right")
    expression_field.grid(columnspan=4, ipadx=90, pady=10)
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('Clear', 5, 0), ('Backspace', 5, 1), ('Quit', 5, 2)
    ]
    for (text, row, col) in buttons:
        Button(gui, text=text, fg="black", bg="white", font=("Arial", 15),
               command=lambda t=text: press(t) if t not in ["Clear", "Backspace", "=", "Quit"] else
               clear() if t == "Clear" else
               backspace() if t == "Backspace" else
               equalpress() if t == "=" else
               close_app(),
               height=2, width=10).grid(row=row, column=col, padx=5, pady=5)
    gui.mainloop()