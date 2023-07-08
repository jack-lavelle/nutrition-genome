import tkinter as tk


class Window:
    title = None
    window = None

    def __init__(self, title) -> None:
        self.window = tk.Tk()
        self.window.title(title)

        # Calculate position
        window_width = 400
        window_height = 300
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))

        # Set size and position
        self.window.geometry(
            f"{window_width}x{window_height}+{x_position}+{y_position}"
        )
