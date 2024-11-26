import tkinter as tk
from tkinter import StringVar, OptionMenu


class LabelEntry(tk.Frame):
    def __init__(self, parent, text, width, options=None):
        super().__init__(parent)
        self.pack(fill=tk.X)
        self.label = text
        self.value = StringVar()

        if options:
            # Dropdown list value
            self.value.set(options[0])
            drop_down = OptionMenu(parent, self.value, *options)
            drop_down.pack()
        else:
            # Self-entered value
            lbl = tk.Label(self, text=text, width=width, anchor='w')
            lbl.pack(side=tk.LEFT, padx=5, pady=5)

            entry = tk.Entry(self)
            entry.pack(side=tk.LEFT, fill=tk.X, padx=5)
            entry.bind('<Return>', self.return_handler)
            self.value = entry

    @staticmethod
    def return_handler(event=None):
        print(f"The RETURN key is pressed")


class Label(tk.Frame):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.pack(fill=tk.X)

        lbl = tk.Label(self, text=text, width=14, anchor='center')
        lbl.pack()

def destroy_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()
