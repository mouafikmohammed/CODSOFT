import tkinter as tk
from tkinter import messagebox
import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
   if os.path.exists(TASKS_FILE):
      with open(TASKS_FILE, 'r') as file:
         return json.load(file)
   return []

# Save tasks to file
def save_tasks():
   tasks = []
   for i in range(task_listbox.size()):
      task_text = task_listbox.get(i)
      completed = task_text.startswith("[✔]")
      title = task_text[4:] if completed else task_text[4:]
      tasks.append({"title": title, "completed": completed})
   with open(TASKS_FILE, 'w') as file:
      json.dump(tasks, file, indent=4)

# Update the listbox display
def update_listbox():
   task_listbox.delete(0, tk.END)
   for task in tasks:
      prefix = "[✔]" if task["completed"] else "[ ]"
      task_listbox.insert(tk.END, f"{prefix} {task['title']}")

# Add a new task
def add_task():
   title = entry.get().strip()
   if title == "":
      messagebox.showwarning("Input Error", "Task cannot be empty.")
      return
   tasks.append({"title": title, "completed": False})
   entry.delete(0, tk.END)
   update_listbox()
   save_tasks()

# Mark task as complete
def complete_task():
   selected = task_listbox.curselection()
   if not selected:
      messagebox.showwarning("Selection Error", "Select a task to mark as complete.")
      return
   index = selected[0]
   tasks[index]["completed"] = not tasks[index]["completed"]
   update_listbox()
   save_tasks()

# Delete task
def delete_task():
   selected = task_listbox.curselection()
   if not selected:
      messagebox.showwarning("Selection Error", "Select a task to delete.")
      return
   index = selected[0]
   tasks.pop(index)
   update_listbox()
   save_tasks()

# Edit task
def edit_task():
   selected = task_listbox.curselection()
   if not selected:
      messagebox.showwarning("Selection Error", "Select a task to edit.")
      return
   index = selected[0]
   current_text = tasks[index]["title"]
   new_title = entry.get().strip()
   if new_title == "":
      messagebox.showwarning("Input Error", "New task name cannot be empty.")
      return
   tasks[index]["title"] = new_title
   entry.delete(0, tk.END)
   update_listbox()
   save_tasks()

# Setup the window
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x450")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10, padx=10, fill=tk.X)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add Task", command=add_task, width=10).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Complete", command=complete_task, width=10).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", command=delete_task, width=10).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Edit", command=edit_task, width=10).grid(row=0, column=3, padx=5)

# Listbox
task_listbox = tk.Listbox(root, font=("Arial", 12), height=15, selectbackground="#a6a6a6")
task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Load and display tasks
tasks = load_tasks()
update_listbox()

# Run the app
root.mainloop()