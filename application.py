import sys
import tkinter as tk
import re
from tkinter import ttk
from functools import partial
from Window import Window
from Person import Person, convert_json_data_to_patients
import Utilities
from CreateReport import create_pdf


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


def initial_gene_selection_driver(window: Window, patient: Person):
    if not patient:
        patient = Person()

    gene_selection_driver(patient, window, 0)

    patients = Utilities.retrieve_json_patient_data()
    if patient.name in patients:
        pattern = re.compile(str(patient.name) + " - [0-9]$")
        name_repetitions = 1
        for key in patients.keys():
            if pattern.match(key):
                name_repetitions += 1
        patient.name = patient.name + " - " + str(name_repetitions)
    patients[patient.name] = patient
    print(patients)


def gene_selection_driver(
    patient: Person,
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

        return


def handle_gene_window(
    patient: Person,
    window: Window,
    iteration_index: int,
    gene_group: list,
):
    gene_master_data = Utilities.load_master_data()

    current_gene_selection = {}

    for gene_section in list(gene_master_data.keys()):
        current_gene_selection[gene_section] = {}

    name = None
    if iteration_index == 0:
        name = tk.Entry(window.window, fg="gray")

        def on_entry_click(event):
            if name.get() == "First and Last Name":
                name.delete(0, tk.END)  # Delete default text
                name.config(fg="black")  # Change text color to black

        def on_focus_out(event):
            if name.get() == "":
                name.insert(0, "First and Last Name")  # Insert default text
                name.config(fg="gray")  # Change text color to gray

        default_text = "First and Last Name"
        name.insert(0, default_text)  # Set initial text
        name.bind("<FocusIn>", on_entry_click)  # Bind click event
        name.bind("<FocusOut>", on_focus_out, name)  # Bind focus out event
        name.pack()

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
            name,
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
    patient: Person,
    window: Window,
    iteration_index: int,
    entry=None,
    genes: dict = None,
):
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

    if entry:
        name = entry.get()
        if name != "First and Last Name":
            patient.name = name
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
        second_window, "Select Patient", [person.name for person in patients]
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


def view_patient_window(window: Window, patient: Person):
    window.window.destroy()
    second_window = Window("View Patient")
    entry = tk.Entry(second_window.window, fg="black")

    entry.insert(0, patient.name)
    entry.config(fg="black")
    entry.pack()

    update_button = ttk.Button(
        second_window.window,
        text="Update Patient - NOT YET IMPLEMENTED",
        command=print("not yet implemented"),
    )
    update_button.pack()

    generate_report_button = ttk.Button(
        second_window.window,
        text="Generate Report",
        command=partial(create_pdf, patient),
    )
    generate_report_button.pack()

    return_home_button = ttk.Button(
        second_window.window,
        text="Return To Home",
        command=partial(return_home, second_window),
    )
    return_home_button.pack()

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
