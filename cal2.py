import tkinter as tk

# Create a function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Create a function to handle the "=" button click
def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create a GUI window
window = tk.Tk()
window.title("Colorful Calculator")

# Create an entry widget for input
entry = tk.Entry(window, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons with labels and assign functions to them
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(window, text=button, padx=20, pady=20, command=calculate, bg='purple', fg='white').grid(row=row_val, column=col_val)
    elif button in '+-*/':
        symbol_button = tk.Button(window, text=button, padx=20, pady=20, font=("Helvetica", 16), command=lambda num=button: button_click(num), bg='orange', fg='white')
        symbol_button.grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, padx=20, pady=20, command=lambda num=button: button_click(num), bg='lightblue').grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the GUI main loop
window.mainloop()
