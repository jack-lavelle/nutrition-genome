import tkinter as tk


def on_entry_click(event):
    if entry.get() == "First and Last Name":
        entry.delete(0, tk.END)  # Delete default text
        entry.config(fg="black")  # Change text color to black


def on_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "First and Last Name")  # Insert default text
        entry.config(fg="gray")  # Change text color to gray


def on_submit():
    name = entry.get()
    if name != "First and Last Name":
        print("Entered name:", name)


root = tk.Tk()

default_text = "First and Last Name"
entry = tk.Entry(root, fg="gray")
entry.insert(0, default_text)  # Set initial text
entry.bind("<FocusIn>", on_entry_click)  # Bind click event
entry.bind("<FocusOut>", on_focus_out)  # Bind focus out event
entry.pack()

button = tk.Button(root, text="Submit", command=on_submit)
button.pack()

root.mainloop()
