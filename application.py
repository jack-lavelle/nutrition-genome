import tkinter as tk
import sys
from tkinter import ttk, Widget
from functools import partial
from Window import Window
from Patient import Patient, convert_json_data_to_patients
import Utilities
import string
from WrappedWidgets import WrappedWidgets


# Screens: 1 - welcome: add new patient, view current patients
def add_green_text(window: Window = None):
    label = tk.Label(window.window, text="")
    label.pack()
    message = "New patient successfully added."
    label.config(text=message, fg="green")


def home_window(
    first_visit: bool = False, patient_added: bool = False, window: Window = None
):
    if not first_visit:
        window.window.destroy()

    root_window = Window("Welcome")

    if patient_added:
        message = "New patient successfully added."
        label = tk.Label(root_window.window, text=message, fg="green")
        label.pack()

    screen2_button = ttk.Button(
        root_window.window,
        text="View Patients",
        command=partial(view_patients, root_window),
    )
    screen2_button.pack()

    screen1_button = ttk.Button(
        root_window.window,
        text="Add a New Patient",
        command=partial(initial_gene_selection_driver, root_window, None),
    )
    screen1_button.pack()
    root_window.window.focus_force()
    root_window.window.mainloop()


def initial_gene_selection_driver(window: Window, patient: Patient):
    if not patient:
        patient = Patient()

    gene_selection_driver(patient, window, 0)


def gene_selection_driver(
    patient: Patient,
    window: Window,
    iteration_index: int,
):
    gene_groups = Utilities.Utilities.categorize_genes()
    window.window.destroy()

    if iteration_index < len(gene_groups):
        # while iteration_index < len(gene_groups), continue to add genes to patient ... not yet
        # done creating patient entry.
        gene_group = gene_groups[iteration_index]
        window = Window(" | ".join(gene_group))
        handle_gene_window(
            patient,
            window,
            iteration_index,
            gene_group,
        )
    else:
        # patient data complete, add them to patients
        # TODO: when editing existing patient, handle existing names and genes.
        json_patient_data = Utilities.retrieve_json_patient_data()
        patients = convert_json_data_to_patients(json_patient_data)
        patients.append(patient)
        Utilities.upload_patients(patients)
        home_window(True, True)


def create_name_widget(window: Window):
    name_widget = tk.Entry(window.window, fg="gray")

    def on_entry_click(event):
        if name_widget.get() == "First and Last Name":
            name_widget.delete(0, tk.END)  # Delete default text
            name_widget.config(fg="black")  # Change text color to black

    def on_focus_out(event):
        if name_widget.get() == "":
            name_widget.insert(0, "First and Last Name")  # Insert default text
            name_widget.config(fg="gray")  # Change text color to gray

    name_widget.insert(0, "First and Last Name")  # Set initial text
    name_widget.bind("<FocusIn>", on_entry_click)  # Bind click event
    name_widget.bind("<FocusOut>", on_focus_out, name_widget)  # Bind focus out event
    name_widget.pack()

    return name_widget


def create_obj_widget(window: Window, objective_int: int):
    default_text = "Personal Objective " + str(objective_int)
    text_widget = tk.Text(window.window, height=2.5, width=25, fg="gray")

    def on_entry_click(event):
        if text_widget.get("1.0", tk.END) == default_text + "\n":
            text_widget.delete("1.0", tk.END)  # Delete default text
            text_widget.config(fg="black")  # Change text color to black

    def on_focus_out(event):
        if text_widget.get("1.0", tk.END) == "\n":
            text_widget.insert(tk.INSERT, default_text)  # Insert default text
            text_widget.config(fg="gray")  # Change text color to gray

    text_widget.insert(tk.INSERT, default_text)  # Set initial text
    text_widget.bind("<FocusIn>", on_entry_click, default_text)  # Bind click event
    text_widget.bind("<FocusOut>", on_focus_out, text_widget)  # Bind focus out event
    text_widget.pack()
    return text_widget


def handle_gene_window(
    patient: Patient,
    window: Window,
    iteration_index: int,
    gene_group: list,
):
    gene_master_data = Utilities.load_master_data()

    current_gene_selection = {}

    for gene_section in list(gene_master_data.keys()):
        current_gene_selection[gene_section] = {}

    # Set patient name and personal objectives if necessary.
    widgets = {}
    name_widget = None
    if not patient.name:
        name_widget = create_name_widget(window)
        widgets["name"] = name_widget

    if not patient.objectives:
        for i in range(1, 4):
            widgets["obj" + str(i)] = create_obj_widget(window, i)

    for gene_section in gene_group:
        genes = list(gene_master_data[gene_section].keys())

        label = tk.Label(window.window, text=gene_section)
        label.pack()

        for gene in genes:
            # avoid duplicating genes in current_selections
            if gene not in current_gene_selection[gene_section]:
                current_gene_selection[gene_section][gene] = tk.BooleanVar()

            checkbox = ttk.Checkbutton(
                window.window,
                text=gene,
                variable=current_gene_selection[gene_section][gene],
            )
            checkbox.pack()

    button = ttk.Button(
        window.window,
        text="Continue",
        command=partial(
            add_patient_action,
            patient,
            window,
            iteration_index,
            widgets,
            current_gene_selection,
        ),
    )
    button.pack()

    return_home_button = ttk.Button(
        window.window,
        text="Return To Home",
        command=partial(return_home, window),
    )
    return_home_button.pack()

    window.resize_window()
    window.window.focus_force()
    window.window.mainloop()


def add_patient_action(
    patient: Patient,
    window: Window,
    iteration_index: int,
    widgets: dict[str, Widget],
    genes: dict = None,
):
    # Close the first window

    selected_genes_dict = {}

    gene_groups = Utilities.Utilities.categorize_genes()

    for gene_section, gene_bool in genes.items():
        if gene_section not in gene_groups[iteration_index]:
            pass
        else:
            for gene, boolean in gene_bool.items():
                if boolean.get():
                    if gene_section not in selected_genes_dict:
                        selected_genes_dict[gene_section] = []

                    selected_genes_dict[gene_section].append(gene)

    # TODO: redo this using WrappedWidgets and for loop widget in widgets (which is now of type
    # WrappedWidgets)
    if widgets:
        name_widget = widgets["name"]
        name = name_widget.get()
        patient.name = name

        objectives = {}
        for i in range(1, 4):
            widget = widgets["obj" + str(i)]
            # This weird code just processes the string, changing \n, \t, \r to " " and strips
            # trailing white space.
            objectives["objective " + str(i)] = (
                widget.get("1.0", tk.END)
                .translate(str.maketrans("\n\t\r", "   "))
                .strip()
            )

        patient.objectives = objectives

    for gene_section in selected_genes_dict:
        patient.genes[gene_section] = selected_genes_dict[gene_section]

    gene_selection_driver(patient, window, iteration_index + 1)


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
        command=partial(add_patient_action, checkboxes),
    )
    button.pack(pady=10)
    checkbox_results = [checkboxes.get(key).get() for key in checkboxes.keys()]

    print(checkbox_results, name)


def get_selected_patient(window: Window, patient_name: str):
    json_patient_data = Utilities.retrieve_json_patient_data()
    patients = convert_json_data_to_patients(json_patient_data)
    patients_dict = {}
    for patient in patients:
        patients_dict[patient.name] = patient

    view_patient_window(window, patients_dict[patient_name.get()])


def view_patients(window: Window):
    json_patient_data = Utilities.retrieve_json_patient_data()
    patients = convert_json_data_to_patients(json_patient_data)

    window.window.destroy()
    second_window = Window("View Patients")
    patient = create_dropdown_menu(
        second_window, "Select Patient", [patient.name for patient in patients]
    )

    button = ttk.Button(
        second_window.window,
        text="Select Patient",
        command=partial(get_selected_patient, second_window, patient),
    )
    button.pack()

    return_home_button = ttk.Button(
        second_window.window,
        text="Return To Home",
        command=partial(return_home, second_window),
    )
    return_home_button.pack()

    second_window.window.focus_force()
    second_window.window.mainloop()


def view_patient_window(window: Window, patient: Patient):
    window.window.destroy()
    second_window = Window("View Patient")
    entry = tk.Entry(second_window.window, fg="black")

    entry.insert(0, patient.name)
    entry.config(fg="black")
    entry.pack()

    total_checkboxes = {}
    print("~~ ERROR ~~ NOT YET IMPLEMENTED")
    sys.exit()
    total_checkboxes = add_new_patient_window({}, second_window, total_checkboxes)

    button = ttk.Button(
        second_window.window,
        text="Update Patient",
        command=partial(add_patient_action, second_window, entry, total_checkboxes),
    )
    button.pack()

    return_home_button = ttk.Button(
        second_window.window,
        text="Return To Home",
        command=partial(return_home, second_window),
    )
    return_home_button.pack()

    second_window.resize_window()
    second_window.window.focus_force()
    second_window.window.mainloop()


def return_home(original_window: Window):
    home_window(False, False, original_window)


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


home_window(True)
