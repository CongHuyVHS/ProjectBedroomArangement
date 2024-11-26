
import tkinter as tk

from UserManager import UserManager
from loginUI import LoginUI


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to Bedroom Arranger tool")
        self.geometry("600x400")

        frame = tk.Frame(self)
        frame.grid(row=0, column=0)

        LoginUI(frame)


if __name__ == '__main__':
    MainWindow().mainloop()


















