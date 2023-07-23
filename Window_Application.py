import tkinter as tk
from tkinter import ttk
from functools import partial
from PIL import Image, ImageTk
from Window import Window
from Person import Person
from Utilities import Utilities

people = []


# Screens: 1 - welcome: add new person, view current people
def add_green_text(window: Window = None):
    label = tk.Label(window.window, text="")
    label.pack()
    message = "New patient successfully added."
    label.config(text=message, fg="green")


def home_window(first_visit=True, window: Window = None):
    root_window = Window("Welcome")
    if not first_visit:
        message = "New patient successfully added."
        label = tk.Label(root_window.window, text=message, fg="green")
        label.pack()

    if window:
        window.window.destroy()

    screen2_button = ttk.Button(
        root_window.window,
        text="View Patients",
        command=partial(view_patients, root_window, people),
    )
    screen2_button.pack()

    screen1_button = ttk.Button(
        root_window.window,
        text="Add a New Patient",
        command=partial(choose_genes_window, root_window),
    )
    screen1_button.pack()
    # ico = Image.open("owm_resources\\logo_icon.png")
    # photo = ImageTk.PhotoImage(ico)
    # root_window.window.wm_iconphoto(False, photo)
    root_window.window.mainloop()


def get_selected_items(window: Window = None, entry=None, selected_genes=None):
    # Close the first window

    selected_items = []
    for item, var in selected_genes.items():
        if var.get():
            selected_items.append(item)

    name = entry.get()
    if name != "First and Last Name":
        print("Entered name:", name)
    print(name, selected_items)

    home_window(False, window)


def choose_genes_window(window: Window = None):
    # Close the first window
    if window:
        properties = window.get_current_properties()
        window.window.destroy()

    second_window = Window("Multi-Select Checkbox")
    entry = tk.Entry(second_window.window, fg="gray")

    def on_entry_click(event):
        if entry.get() == "First and Last Name":
            entry.delete(0, tk.END)  # Delete default text
            entry.config(fg="black")  # Change text color to black

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, "First and Last Name")  # Insert default text
            entry.config(fg="gray")  # Change text color to gray

    default_text = "First and Last Name"
    entry.insert(0, default_text)  # Set initial text
    entry.bind("<FocusIn>", on_entry_click)  # Bind click event
    entry.bind("<FocusOut>", on_focus_out, entry)  # Bind focus out event
    entry.pack()

    total_checkboxes = {}
    total_checkboxes = add_and_select_genes({}, second_window, total_checkboxes)

    button = ttk.Button(
        second_window.window,
        text="Submit",
        command=partial(get_selected_items, second_window, entry, total_checkboxes),
    )
    button.pack(pady=10)

    second_window.resize_window()
    second_window.window.mainloop()


def add_and_select_genes(current_selections, window, total_selections):
    gene_master_data = Utilities.load_master_data()

    gene_sections = list(gene_master_data.keys())
    for gene_section in gene_sections:
        genes = list(gene_master_data[gene_section].keys())

        label = tk.Label(window.window, text=gene_section)
        label.pack()

        for gene in genes:
            current_selections[gene] = tk.BooleanVar()
            checkbox = ttk.Checkbutton(
                window.window, text=gene, variable=current_selections[gene]
            )
            checkbox.pack()

        total_selections = current_selections | total_selections

    return total_selections


def add_title_checkboxes(
    title: str, options: list, window: Window, total_checkboxes: dict
):
    label = tk.Label(window.window, text=title)
    label.pack()

    checkboxes = {}
    for option in options:
        checkboxes[option] = tk.BooleanVar()
        checkbox = ttk.Checkbutton(
            window.window, text=option, variable=checkboxes[option]
        )
        checkbox.pack()

    total_checkboxes = checkboxes | total_checkboxes


def handle_button_click(name, window, checkboxes):
    name_box = ttk.Entry(window.window)
    name_box.pack()
    name = name_box.get()

    button = ttk.Button(
        window.window,
        text="Submit Genes",
        command=partial(get_selected_items, checkboxes),
    )
    button.pack(pady=10)
    checkbox_results = [checkboxes.get(key).get() for key in checkboxes.keys()]

    print(checkbox_results, name)


def get_selected_patient(window: Window, patient):
    print(patient.get())


def view_patients(window: Window, patients: list):
    window_backup = window
    if not people:
        person1 = Person("Name 1", "Mood / Memory")
        person2 = Person("Name 2")
        people.extend([person1, person2])

    second_window = Window("View Patients")
    patient = create_dropdown_menu(second_window, "Brain Health", people)

    button = ttk.Button(
        second_window.window,
        text="Select Patient",
        command=partial(get_selected_patient, second_window, patient),
    )
    button.pack(pady=10)

    window.window.destroy()
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


home_window()
