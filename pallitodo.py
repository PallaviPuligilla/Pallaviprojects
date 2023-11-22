import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def _init_(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []

        # Entry fields
        self.description_entry = tk.Entry(self.master, width=30)
        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.master, height=10, width=50)

        # Buttons
        self.complete_button = tk.Button(self.master, text="Mark Completed", command=self.mark_completed)
        self.remove_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)

        # Pack widgets
        self.description_entry.pack(pady=5)
        self.add_button.pack(pady=5)
        self.task_listbox.pack(pady=5)
        self.complete_button.pack(pady=5)
        self.remove_button.pack(pady=5)

    def add_task(self):
        description = self.description_entry.get()
        if description:
            self.tasks.append(description)
            self.update_task_listbox()
            self.clear_entry_fields()
        else:
            messagebox.showwarning("Warning", "Please enter a task description.")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            self.tasks[task_index] = f"[Completed] {self.tasks[task_index]}"
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def clear_entry_fields(self):
        self.description_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()

# Initialize the To-Do List App
app = ToDoApp()

# Run the application
root.mainloop()