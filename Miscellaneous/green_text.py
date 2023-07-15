import tkinter as tk


def add_green_text():
    message = "New patient successfully added."
    label.config(text=message, fg="green")


root = tk.Tk()

label = tk.Label(root, text="")
label.pack()

button = tk.Button(root, text="Add Green Text", command=add_green_text)
button.pack()

root.mainloop()
