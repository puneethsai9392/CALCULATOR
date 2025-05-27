from tkinter import *
import math

expression = ""

def press(key):
    global expression
    if key == "x²":
        expression += "^2"
    elif key in ["π", "√", "log", "ln", "sin", "cos", "tan"]:
        expression += key + "(" if key not in ["x²", "π"] else key
    else:
        expression += str(key)
    equation.set(expression)

def equalpress():
    global expression
    try:
        # Convert readable symbols to math functions
        to_eval = expression.replace("π", "math.pi") \
                            .replace("√", "math.sqrt") \
                            .replace("^", "**") \
                            .replace("log", "math.log10") \
                            .replace("ln", "math.log") \
                            .replace("sin", "math.sin") \
                            .replace("cos", "math.cos") \
                            .replace("tan", "math.tan")
        result = str(eval(to_eval))
        equation.set(result)
        expression = ""
    except Exception:
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
    if event.char in "0123456789.+-*/()":
        press(event.char)
    elif event.keysym == "Return":
        equalpress()
    elif event.keysym == "BackSpace":
        backspace()

# GUI setup
gui = Tk()
gui.configure(bg="#1e1e1e")
gui.title("Scientific Calculator")
gui.geometry("400x600")
gui.resizable(False, False)

equation = StringVar()
expression_field = Entry(gui, textvariable=equation, font=("Arial", 24),
                         bg="#1e1e1e", fg="white", bd=0, justify="right",
                         insertbackground="white")
expression_field.grid(row=0, column=0, columnspan=5, ipadx=8, ipady=20, pady=15, padx=10, sticky="we")
expression_field.focus_set()

gui.bind("<Key>", key_press)

# Button layout: (text, row, col, bg)
buttons = [
    ("C", 1, 0, "#ff5c5c"), ("⌫", 1, 1, "#555555"), ("(", 1, 2, "#555555"), (")", 1, 3, "#555555"), ("OFF", 1, 4, "#ff3b30"),
    ("sin", 2, 0, "#333333"), ("cos", 2, 1, "#333333"), ("tan", 2, 2, "#333333"), ("log", 2, 3, "#333333"), ("ln", 2, 4, "#333333"),
    ("7", 3, 0, "#2e2e2e"), ("8", 3, 1, "#2e2e2e"), ("9", 3, 2, "#2e2e2e"), ("/", 3, 3, "#ff9500"), ("√", 3, 4, "#333333"),
    ("4", 4, 0, "#2e2e2e"), ("5", 4, 1, "#2e2e2e"), ("6", 4, 2, "#2e2e2e"), ("*", 4, 3, "#ff9500"), ("x²", 4, 4, "#333333"),
    ("1", 5, 0, "#2e2e2e"), ("2", 5, 1, "#2e2e2e"), ("3", 5, 2, "#2e2e2e"), ("-", 5, 3, "#ff9500"), ("π", 5, 4, "#333333"),
    ("0", 6, 0, "#2e2e2e"), (".", 6, 1, "#2e2e2e"), ("=", 6, 2, "#00cc66"), ("+", 6, 3, "#ff9500"),
]

def handle_button(text):
    expression_field.focus_set()
    if text == "C":
        clear()
    elif text == "⌫":
        backspace()
    elif text == "=":
        equalpress()
    elif text == "OFF":
        close_app()
    else:
        press(text)

# Create and place buttons
for (text, row, col, color) in buttons:
    btn = Button(gui, text=text, bg=color, fg="white", font=("Helvetica", 16, "bold"),
                 bd=0, width=5, height=2, command=lambda t=text: handle_button(t),
                 activebackground="#666")
    btn.grid(row=row, column=col, padx=5, pady=5)

# Fill remaining grid cell if needed
Button(gui, text="", state=DISABLED, bg="#1e1e1e").grid(row=6, column=4)

# Equal spacing
for i in range(7):
    gui.grid_rowconfigure(i, weight=1)
for j in range(5):
    gui.grid_columnconfigure(j, weight=1)

gui.mainloop()
