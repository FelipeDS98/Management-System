from tkinter import *


class Window:
    def __init__(self, r):
        self.r = r

    def win(self, w, h, x, y):
        self.r.resizable(False, False)
        screen_height = self.r.winfo_screenheight()
        screen_width = self.r.winfo_screenwidth()
        x_coordinate = int((screen_width / 2) - (w / 2))
        y_coordinate = int((screen_height / 2) - (h / 2))

        x_coordinate += x
        y_coordinate -= y

        self.r.geometry("{}x{}+{}+{}".format(w, h, x_coordinate, y_coordinate))
        return self.r

