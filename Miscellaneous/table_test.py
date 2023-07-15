import tkinter as tk
from tkinter import ttk
from Window import Window

window1 = Window("Title")
window = window1.window

# Create a container frame
frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)


def create_table(window):
    style1 = ttk.Style()
    style1.configure("Treeview", rowheight=25)
    tree1 = ttk.Treeview(frame, style="Treeview")
    tree1["columns"] = ("Name", "Age", "City")
    tree1.column("#0")
    tree1.column("Name")
    tree1.column("Age")
    tree1.column("City")
    tree1.heading("#0", text="ID")
    tree1.heading("Name", text="Name")
    tree1.heading("Age", text="Age")
    tree1.heading("City", text="City")
    tree1.insert(parent="", index="end", text="1", values=("John Doe", 30, "New York"))
    tree1.insert(parent="", index="end", text="2", values=("Jane Smith", 25, "London"))
    tree1.insert(parent="", index="end", text="3", values=("Bob Johnson", 35, "Paris"))
    tree1.pack(fill="both")


create_table(window)
create_table(window)


# Start the Tkinter event loop
window.mainloop()
