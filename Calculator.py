import tkinter as tk
from tkinter import messagebox

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

def on_button_click(char):
    if char == "=":
        expression = entry.get()
        result = evaluate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    elif char == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, char)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, font=('Arial', 24), bd=8, insertwidth=4, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '1', '2', '3', '/', 
    '4', '5', '6', '*', 
    '7', '8', '9', '-', 
    '0', '.', '=', '+',
    'C'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: on_button_click(x)
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
