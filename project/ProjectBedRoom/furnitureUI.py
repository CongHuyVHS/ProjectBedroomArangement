import tkinter as tk
from tkinter import ttk, Toplevel
from BedFactory import BedFactory
from ClosetFactory import ClosetFactory
from DrawerFactory import DrawerFactory
from NightStandFactory import NightStandFactory
from OfficeTableFactory import OfficeTableFactory
from Bed import Bed
from Drawer import Drawer
from utils import LabelEntry, Label

class ControlButton(tk.Frame):
    def __init__(self, parent, furniture_name, entries, furniture_factory = None, bedroom_name = None):
        super().__init__(parent)
        self.pack(fill=tk.X)
        self.furniture_name = furniture_name
        self.entries = entries
        self.furniture_factory = furniture_factory
        self.bedroom_name = bedroom_name
        save_button = tk.Button(self, text="Save", command=self.save_info)
        save_button.pack(side=tk.RIGHT)

    def save_info(self):

        for index in range(len(self.entries)):
            name = self.furniture_name + str(index+1)
            furniture_type = self.entries[index].value.get()
            if index == 0:
                self.furniture_factory[self.furniture_name].clear_furniture()
            if furniture_type != "none":
                if self.furniture_name == "Bed":
                    bed = Bed(name, furniture_type)
                    self.furniture_factory[self.furniture_name].add_furniture(bed, name)
                elif self.furniture_name == "Drawer":
                    drawer = Drawer(name, furniture_type)
                    self.furniture_factory[self.furniture_name].add_furniture(drawer, name)

        print(f"show furniture for bedroom {self.bedroom_name}")
        self.furniture_factory[self.furniture_name].show_furniture()


class BedUI(tk.Frame):
    def __init__(self, parent, furniture_factory, bedroom_name):
        super().__init__(parent)

        max_beds = 3
        entries = []  # A list of tuple(name, LabelEntry)
        fields = ["Bed type"]
        options = ["none", "single", "double", "queen", "king"]

        for bed in range(1, max_beds + 1):
            bed_name = "Bed-"+str(bed)
            Label(parent, bed_name)
            for field in fields:
                entries.append(LabelEntry(parent, field, width=10, options=options))

        ControlButton(parent, "Bed", entries=entries, furniture_factory=furniture_factory, bedroom_name = bedroom_name)


class DrawerUI(tk.Frame):
    def __init__(self, parent,furniture_factory,bedroom_name):
        super().__init__(parent)

        max_drawers = 3
        entries = []  # A list of tuple(name, LabelEntry)
        fields = ["Drawer type"]
        options = ["none", "3 drawers", "4 drawers"]

        for drawer in range(1, max_drawers + 1):
            drawer_name = "Drawer-"+str(drawer)
            Label(parent, drawer_name)
            for field in fields:
                entries.append(LabelEntry(parent, field, width=10, options=options))

        ControlButton(parent, "Drawer", entries=entries,furniture_factory=furniture_factory, bedroom_name = bedroom_name)


class ClosetUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        max_closets = 2
        entries = []  # A list of tuple(name, LabelEntry)
        fields = ["Closet type"]
        options = ["none", "small(24Wx72Lx24H)", "medium(36Wx72Lx24H)", "large(48Wx72Lx24H)"]

        for closet in range(1, max_closets + 1):
            closet_name = "Closet-"+str(closet)
            Label(parent, closet_name)
            for field in fields:
                entries.append(LabelEntry(parent, field, width=10, options=options))

        ControlButton(parent, "Closet", entries=entries)


class NightStandUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        max_night_stands = 2
        entries = []  # A list of tuple(name, LabelEntry)
        fields = ["Night stand type"]
        options = ["none", "small(18Wx14Lx24H)", "medium(18Wx14Lx24H)", "large(18Wx14Lx24H)"]

        for night_stand in range(1, max_night_stands + 1):
            night_stand_name = "Night stand-"+str(night_stand)
            Label(parent, night_stand_name)
            for field in fields:
                entries.append(LabelEntry(parent, field, width=10, options=options))

        ControlButton(parent, "Night stand", entries=entries)

class OfficeTableUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        max_office_table = 2
        entries = []  # A list of tuple(name, LabelEntry)
        fields = ["Office table type"]
        options = ["none", "small(40Wx20Lx28H)", "medium(40Wx20Lx28H)", "large(40Wx20Lx28H)"]

        for office_table in range(1, max_office_table + 1):
            office_table_name = "Office table-"+str(office_table)
            Label(parent, office_table_name)
            for field in fields:
                entries.append(LabelEntry(parent, field, width=10, options=options))

        ControlButton(parent, "Office table", entries=entries)

class FurnitureUI():
    def __init__(self, bedroom):
        self.root = Toplevel()
        self.root.title(f"Furniture for {bedroom.name}'s bedroom")
        self.root.geometry("600x400")
        tab_control = ttk.Notebook(self.root)
        tab_control.pack(expand=1, fill="both")

        furniture = ["Bed", "Drawer", "Closet", "Night stand", "Office table", "Result"]

        self.furniture_factory = {}
        bed_factory = BedFactory()
        self.furniture_factory[furniture[0]] = bed_factory

        closet_factory = ClosetFactory()
        self.furniture_factory[furniture[2]] = closet_factory

        drawer_factory = DrawerFactory()
        self.furniture_factory[furniture[1]] = drawer_factory

        night_stand_factory = NightStandFactory()
        self.furniture_factory[furniture[3]] = night_stand_factory

        office_table_factory = OfficeTableFactory()
        self.furniture_factory[furniture[4]] = office_table_factory

        for item in furniture:
            tab = ttk.Frame(tab_control)
            tab_control.add(tab, text =f"{item}")

            if item == "Bed":
                BedUI(tab, self.furniture_factory, bedroom.name)
            elif item == "Drawer":
                DrawerUI(tab, self.furniture_factory,bedroom.name)
            elif item == "Closet":
                ClosetUI(tab)
            elif item == "Night stand":
                NightStandUI(tab)
            elif item == "Office table":
                OfficeTableUI(tab)
            elif item == "Result":
                # Invoke bedroom arranger logic
                pass

    def start_mainloop(self):
        self.root.mainloop()