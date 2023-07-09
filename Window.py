import tkinter as tk


class Window:
    title = None
    window = None
    properties = None
    persons = None

    def __init__(self, title, properties=None) -> None:
        self.window = tk.Tk()
        self.window.title(title)

        if not properties:
            window_width = 400
            window_height = 300
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            x_position = int((screen_width / 2) - (window_width / 2))
            y_position = int((screen_height / 2) - (window_height / 2))

            self.window.geometry(
                f"{window_width}x{window_height}+{x_position}+{y_position}"
            )
        else:
            window_width = 400
            window_height = 300
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            x_position = int((screen_width / 2) - (window_width / 2))
            y_position = int((screen_height / 2) - (window_height / 2))

            self.window.geometry(
                f"{window_width}x{window_height}+{x_position}+{y_position}"
            )

    def set_geometry(self, properties=None):
        self.properties = self.get_current_properties()
        self.window.geometry(
            f"{properties[0][0]}x{properties[0][1]}+{properties[1][0]}+{properties[1][1]}"
        )

    def calculate_current_position(self):
        window_width = 400
        window_height = 300
        window_properties = [window_width, window_height]

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        screen_properties = [screen_width, screen_height]

        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))
        coordinate_position_properties = [x_position, y_position]

        return [window_properties, screen_properties, coordinate_position_properties]

    def set_position(self, properties_list):
        window_width = properties_list[0][0]
        window_height = properties_list[0][1]

        x_position = properties_list[1][0]
        y_position = properties_list[1][1]

        self.window.geometry(
            f"{window_width}x{window_height}+{x_position}+{y_position}"
        )

    def calculate_screen_position_original(self):
        window_width = 400
        window_height = 300
        window_properties = [window_width, window_height]

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        screen_properties = [screen_width, screen_height]

        x_position = int((screen_width / 2) - (window_width / 2))
        y_position = int((screen_height / 2) - (window_height / 2))
        coordinate_position_properties = [x_position, y_position]

        return [window_properties, screen_properties, coordinate_position_properties]

    def get_current_properties(self):
        if not self.properties:
            return self.calculate_current_position()
        return self.properties