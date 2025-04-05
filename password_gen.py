import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4 or length > 20:
            messagebox.showwarning("Too Short or Too Long", "Password length should be at least 4 characters or not more 20 characters.")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        password_var.set(password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Copy to clipboard
def copy_password():
    pwd = password_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("350x250")
root.resizable(False, False)

# Length input
tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 14), justify='center')
length_entry.pack()

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="lightgreen").pack(pady=10)

# Password display
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), justify="center", state="readonly", width=30).pack(pady=10)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_password, font=("Arial", 12), bg="lightblue").pack(pady=5)

# Run GUI
root.mainloop()
