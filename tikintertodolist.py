import tkinter as tk
from tkinter import ttk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        updated_task = entry.get()
        if updated_task:
            listbox.delete(selected_task_index)
            listbox.insert(selected_task_index, updated_task)
            entry.delete(0, tk.END)

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)

def mark_completed():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        task = listbox.get(selected_task_index)
        completed_listbox.insert(tk.END, task)
        listbox.delete(selected_task_index)

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Use ttk style for a more modern look
style = ttk.Style()

# Customize the background to light blue
style.configure("TFrame", background="#ADD8E6")
style.configure("TButton", padding=6, relief="flat", background="#87CEEB")
style.configure("TEntry", padding=6, relief="flat", background="white")

# Create input entry and buttons
entry = ttk.Entry(window, width=30)
add_button = ttk.Button(window, text="Add Task", command=add_task)
update_button = ttk.Button(window, text="Update Task", command=update_task)
delete_button = ttk.Button(window, text="Delete Task", command=delete_task)
complete_button = ttk.Button(window, text="Mark Completed", command=mark_completed)

# Create task list and completed task list
listbox = tk.Listbox(window, selectmode=tk.SINGLE)
completed_listbox = tk.Listbox(window, selectmode=tk.SINGLE)

# Place widgets on the window
entry.pack(pady=10)
add_button.pack(pady=5)
update_button.pack(pady=5)
delete_button.pack(pady=5)
complete_button.pack(pady=5)
listbox.pack(pady=10)
completed_listbox.pack()

# Run the main loop
window.mainloop()