import tkinter as tk
from tkinter import ttk

# Create the first window
root = tk.Tk()
root.title("Main Window")

# Button to open the second window
button = ttk.Button(root, text="Add a new person", command=open_second_window)
button.pack()

root.mainloop()
