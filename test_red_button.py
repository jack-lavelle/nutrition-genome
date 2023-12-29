import tkinter as tk
from tkinter import ttk


def show_color(color):
    new_window = tk.Toplevel(root)
    new_window.title(color)
    new_window.geometry("100x100")
    new_window.configure(background=color)


def on_button_click():
    show_color(color_name)


root = tk.Tk()

color_name = "red"
selected_colors = {color_name: tk.BooleanVar()}

button = ttk.Button(root, text=color_name, cursor="hand2", command=on_button_click)
button.pack(padx=10, pady=10)

checkbox = ttk.Checkbutton(root, text=color_name, variable=selected_colors[color_name])
checkbox.pack(padx=10, pady=10)

root.mainloop()
