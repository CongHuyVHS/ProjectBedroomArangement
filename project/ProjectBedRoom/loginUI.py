import tkinter as tk
from utils import *
from accountUI import AccountUI
from bedroomUI import BedRoomUI
from globalVar import user_manager
from tkinter import messagebox


class ControlButton(tk.Frame):
    def __init__(self, parent, entries):
        super().__init__(parent)
        self.pack(fill=tk.X)

        self.parent = parent
        self.entries = entries

        ok_button = tk.Button(self, text="Login", command=self.verify_user)
        ok_button.pack(side=tk.RIGHT, padx=5, pady=5)

        register_button = tk.Button(self, text="Register", command=self.create_account)
        register_button.pack(side=tk.RIGHT)

    def verify_user(self):
        username = self.entries[0].value.get()
        password = self.entries[1].value.get()
        print(f"Verify user credential for user: {username} with pwd: {password}")
        if username in user_manager.users:
            if password == user_manager.users[username].password:
                user = user_manager.users[username]
                destroy_widgets(self.parent)
                BedRoomUI(self.parent, user)
            else:
                messagebox.showerror("ERROR","Password is invalid")
        else:
            messagebox.showerror("ERROR","Username is invalid")
        # # Once the user authentication is verified, load 'bedroom' UI
        # destroy_widgets(self.parent)
        # ### to do
        # BedRoomUI(self.parent, None)

    def create_account(self):
        print(f"Create new user account")

        # Destroy the Login widgets and load Account UI
        destroy_widgets(self.parent)
        AccountUI(self.parent)


class LoginUI(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        entries = []
        fields = ["Username", "Password"]
        for field in fields:
            entries.append(LabelEntry(parent, field, width=10))

        self.button = ControlButton(parent, entries)
