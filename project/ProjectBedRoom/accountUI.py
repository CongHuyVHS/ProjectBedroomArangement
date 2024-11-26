import tkinter as tk
from globalVar import user_manager
from utils import *
from bedroomUI import BedRoomUI
from tkinter import messagebox
from User import User
import re

class ControlButton(tk.Frame):
    def __init__(self, parent, entries):
        super().__init__(parent)
        self.pack(fill=tk.X)

        self.parent = parent
        self.entries = entries

        save_button = tk.Button(self, text="Save", command=self.create_account)
        save_button.pack(side=tk.RIGHT)

    def create_account(self):
        username = self.entries[0].value.get()
        password = self.entries[1].value.get()
        email = self.entries[2].value.get()
        print(f"Verify user credential for user: {username} with pwd: {password} and email: {email}")
        if self.validate_user(username, password, email):
            user = User(username, password, email)
            user_manager.add_user(user)
            user_manager.show_users()

            # Once the user inputs are validated, load the 'bedroom' UI
            destroy_widgets(self.parent)
            BedRoomUI(self.parent, user)

    @staticmethod
    def validate_user(username, password, email):
        if len(username) < 6:
            messagebox.showerror("ERROR", "Username must be at least 6 characters long")
            return False

        if len(password) < 10:
            messagebox.showerror("ERROR", "Password must be at least 10 characters long")
            return False

        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
        if not valid:
            messagebox.showerror("ERROR", "Email is invalid")
            return False
        return True

class AccountUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        entries = []
        fields = ["Username", "Password", "Email"]
        for field in fields:
            entries.append(LabelEntry(parent, field, width=10))

        ControlButton(parent, entries)
