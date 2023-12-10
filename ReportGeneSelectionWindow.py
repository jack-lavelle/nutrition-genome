import json
from Window import Window
import tkinter as tk
from functools import partial

from Utilities import get_gene_info
from Gene import Gene


class ReportGeneSelectionWindow(Window):
    """This is the window that handles selecting the genes to be included in the report.

    Attributes:
        selected_genes (`dict[str, list[Gene]]`): Starts empty and then fills as genes are selected.
        This has data that looks like:
            {
                "objective1" : ("Gene1", "Gene2"),
                "objective2" : ("Gene1", "Gene2"),
                "objective3" : ("Gene1", "Gene2")
            }
    """

    selected_genes_category: dict[str, list[Gene]] = {}
    INITIAL_OBJECTIVE_X_Y = (25, 15)
    SUGGESTED_ROW_COLUMN = (1, 1)

    def __init__(self, objectives, root) -> None:
        super().__init__("Report Gene Selection", None, None)
        self.objectives = objectives
        x, y = self.INITIAL_OBJECTIVE_X_Y
        # TODO: right now we want only one gene to be added.
        # for objective in objectives:
        #    self.add_objective_section(objective)
        self.add_objective_section("Objective 1: Improve sleep.", x, y)

    def add_objective_section(self, objective: str, x0: int, y0: int):
        """This is called from application.py and adds a gene selection section corresponding to a
        single objective with both automatic and manual selection types (automatic corresponding to
        genes chosen from natural language processing).
        """
        tk.Label(self.window, text=objective, fg="black").place(x=x0, y=y0)
        self.create_automatic_selection_list_widget(objective, x0 + 20, y0 + 20)
        self.create_manual_selection_list_widget(objective)

    # Join these methods
    def create_automatic_selection_list_widget(
        self, objective: str, x0: int, y0: int
    ) -> dict[str, bool]:
        # genes = get_similarity_dict(objective)

        # sample dict output from get_similarity_dict using objective: "Improve sleep"
        tk.Label(self.window, text="Suggested Relevant Genes", fg="black").place(
            x=x0, y=y0
        )
        genes = dict(
            [
                (
                    "FUT2",
                    {
                        "Similarity": 0.6205169558525085,
                        "Significance": "Lower Gaba production: sleep / calm hormone",
                        "Category": "Mood / Memory",
                    },
                ),
                (
                    "GAD1",
                    {
                        "Similarity": 0.6171880960464478,
                        "Significance": "Lower GABA-sleep/calm hormone",
                        "Category": "Mood / Memory",
                    },
                ),
                (
                    "MTHFR 1298",
                    {
                        "Similarity": 0.6098900437355042,
                        "Significance": "Higher need for folate for healthier Nitric Oxide production( inflammation reduction, blood pressure control, brain function, and cancer protection)",
                        "Category": "General Inflammation",
                    },
                ),
            ]
        )
        tk.Label(
            self.window,
            text=f"Gene Name, Percent Relevancy",
            anchor="w",
        ).place(x=x0 + 35, y=y0 + 20)
        selected_genes = {}
        for count, gene_name in enumerate(genes):
            if gene_name not in selected_genes:
                selected_genes[gene_name] = tk.BooleanVar()
            gene_data = genes[gene_name]
            tk.Checkbutton(self.window, variable=selected_genes[gene_name]).place(
                x=x0 + 15, y=y0 + (count + 2) * 20
            )
            gene_label = tk.Label(
                self.window,
                text=f"{gene_name}, {round(gene_data['Similarity'] * 100, 2)}",
                anchor="w",
            )
            gene_label.bind(
                "<Enter>", lambda bind_enter, label=gene_label: label.config(fg="blue")
            )
            gene_label.bind(
                "<Leave>", lambda bind_leave, label=gene_label: label.config(fg="black")
            )
            gene_label.bind(
                "<Button-1>",
                lambda get_info, gene_name=gene_name: self.test_func(gene_name),
            )
            gene_label.place(x=x0 + 35, y=y0 + (count + 2) * 20)

    def create_manual_selection_list_widget(self, objective: str) -> set[Gene]:
        # manual gene selection
        pass

    def test_func(self, gene_name: str):
        gene_data_window = Window(f"{gene_name}" + " Information", root=self.root)
        tk.Label(
            gene_data_window.window,
            text=json.dumps(get_gene_info(gene_name)),
            wraplength=200,
        ).pack()
        gene_data_window.window.mainloop()
