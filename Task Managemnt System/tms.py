import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except tk.TclError:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")

# Create the main window
window = tk.Tk()
window.title("Task Management System")

# Create the task entry field
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=10)

# Create the "Add Task" button
add_btn = tk.Button(window, text="Add Task", command=add_task)
add_btn.pack(pady=5)

# Create the task listbox
listbox = tk.Listbox(window, font=("Arial", 12), width=50)
listbox.pack(padx=20, pady=10)

# Create the "Delete Task" button
delete_btn = tk.Button(window, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

# Start the main event loop
window.mainloop()
