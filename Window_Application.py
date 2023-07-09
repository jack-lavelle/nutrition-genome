import tkinter as tk
from tkinter import ttk
from functools import partial
from PIL import Image, ImageTk
from Window import Window

# Screens: 1 - welcome: add new person, view current people


def home_window():
    root_window = Window("Welcome")

    screen1_button = ttk.Button(
        root_window.window,
        text="Add a New Patient",
        command=partial(add_view_patients, root_window),
    )
    screen1_button.pack()

    screen2_button = ttk.Button(
        root_window.window,
        text="View Patients",
        command=partial(open_screen2_window, root_window),
    )
    screen2_button.pack()

    ico = Image.open("owm_resources\\logo_icon.png")
    photo = ImageTk.PhotoImage(ico)
    root_window.window.wm_iconphoto(False, photo)
    root_window.window.mainloop()


def add_view_patients(window: Window):
    # Close the first window
    properties = window.get_current_properties()
    window.window.destroy()

    # Create the second window
    second_window = Window("Add a New Patient", properties)

    # Name Entry
    name_label = ttk.Label(second_window.window, text="Enter Name:")
    name_label.pack()
    name_entry = ttk.Entry(second_window.window)
    name_entry.pack()

    # Dropdown Menu
    dropdown_label = ttk.Label(second_window.window, text="Choose Genes:")
    dropdown_label.pack()
    dropdown = ttk.Combobox(second_window.window, values=["Item 1", "Item 2", "Item 3"])
    dropdown.pack()

    # Button
    button = ttk.Button(
        second_window.window,
        text="Submit",
        command=partial(add_view_patients, second_window),
    )
    button.pack()

    second_window.window.mainloop()


def open_screen2_window(window: Window):
    pass


home_window()
