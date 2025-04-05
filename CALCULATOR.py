import tkinter as tk
from tkinter import messagebox

# Perform calculation
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Setup GUI
root = tk.Tk()
root.title("🧮 Simple Calculator")
root.geometry("300x300")
root.resizable(False, False)

# Input fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 14))
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 14))
entry2.pack(pady=5)

# Operation selection
tk.Label(root, text="Choose Operation:").pack(pady=5)
operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]
tk.OptionMenu(root, operation_var, *operations).pack(pady=5)

# Calculate button
tk.Button(root, text="Calculate", command=calculate, font=("Arial", 12), bg="lightblue").pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
