import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../../nutrition-genome")
from ReportGeneSelectionWindow import ReportGeneSelectionWindow

test_window = ReportGeneSelectionWindow(
    ["Improve sleep", "Lose weight", "Decrease stress"], None
)

test_window.window.mainloop()
