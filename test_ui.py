import tkinter as tk
from tkinter import ttk
from functools import partial
from Window import Window


def open_second_window(root):
    # Close the first window
    root.destroy()

    # Create the second window
    second_window = Window("Add a new person.")

    # Name Entry
    name_label = ttk.Label(second_window.window, text="Enter Name:")
    name_label.pack()
    name_entry = ttk.Entry(second_window.window)
    name_entry.pack()

    # Dropdown Menu
    dropdown_label = ttk.Label(second_window.window, text="Choose Item:")
    dropdown_label.pack()
    dropdown = ttk.Combobox(second_window.window, values=["Item 1", "Item 2", "Item 3"])
    dropdown.pack()

    # Button
    button = ttk.Button(second_window.window, text="Submit")
    button.pack()

    second_window.window.mainloop()


def open_home_window():
    root_window = Window("Welcome")

    # Button to open the second window
    button = ttk.Button(
        root_window.window,
        text="Add a new person",
        command=partial(open_second_window, root_window.window),
    )
    button.pack()

    root_window.window.mainloop()


open_home_window()
