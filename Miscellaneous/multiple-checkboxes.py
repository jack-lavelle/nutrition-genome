from functools import partial
import tkinter as tk
from tkinter import ttk
from Window import Window


def get_selected_items(checkboxes, results):
    selected_items = []
    for item, var in checkboxes.items():
        if var.get():
            selected_items.append(item)

    print(selected_items, results.get())


def choose_genes_window(window: Window = None):
    # Close the first window
    if window:
        properties = window.get_current_properties()
        window.window.destroy()

    second_window = Window("Multi-Select Checkbox")
    options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    results = create_dropdown_menu(second_window, second_window.title, options)

    checkboxes = {}
    for option in options:
        checkboxes[option] = tk.BooleanVar()
        checkbox = ttk.Checkbutton(
            second_window.window, text=option, variable=checkboxes[option]
        )
        checkbox.pack()

    button = ttk.Button(
        second_window.window,
        text="Choose Genes",
        command=partial(get_selected_items, checkboxes, results),
    )
    button.pack(pady=10)

    second_window.window.mainloop()


def create_dropdown_menu(window: Window, title: str, options: list):
    selected_option = tk.StringVar()
    selected_option.set(title)

    dropdown = ttk.Combobox(
        window.window,
        values=options,
        textvariable=selected_option,
        state="readonly",
    )
    dropdown.pack()
    return selected_option


choose_genes_window()
