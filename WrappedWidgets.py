import tkinter as tk
from tkinter import Widget


class WrappedWidgets:
    def __init__(self, widget: Widget) -> None:
        self.widget = widget

    def pack(self):
        self.widget.pack()

    def get(self):
        match type(self.widget):
            case tk.Text:
                return self.widget.get("1.0", tk.END)
            case _:
                return self.widget.get()
