import tkinter as tk
from tkinter import ttk


class ClickableTextButton(tk.Frame):
    def __init__(self, parent, gene_name_similarity, checkbox_variable):
        tk.Frame.__init__(self, parent)
