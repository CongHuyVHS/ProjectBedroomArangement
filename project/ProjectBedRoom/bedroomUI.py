import tkinter as tk
from BedroomManager import BedRoomManager
from BedRoom import BedRoom
from globalVar import user_manager
from utils import LabelEntry, Label, destroy_widgets
from furnitureUI import FurnitureUI


class ControlButton(tk.Frame):
    def __init__(self, parent, entries, max_rooms, user):
        super().__init__(parent)
        self.pack(fill=tk.X)
        self.furniture_started = False
        self.parent = parent
        self.entries = entries
        self.nb_rooms = max_rooms
        self.user = user

        save_button = tk.Button(self, text="Save", command=self.save_info)
        save_button.pack(side=tk.RIGHT)

    def save_info(self):
        if self.furniture_started:
            return

        self.furniture_started = True
        rooms = []
        for room in range(self.nb_rooms):
            index = room*3  # Each room has 3 entries (name, size, free-space)
            room_name = self.entries[index].value.get()
            room_size = self.entries[index+1].value.get()
            room_free_percent = self.entries[index+2].value.get()
            if room_name:
                rooms.append((room_name, room_size,room_free_percent))

        bedroom_manager =  BedRoomManager()

        # Once the user inputs are validated, load the 'furniture' UI for each bedroom
        handlers = []       # A list of Furniture objects
        for room in rooms:
            user_manager.add_bedroom_to_user(self.user, bedroom_manager)
            dimension = room[1].split("x")

            bedroom = BedRoom(room[0], dimension[0], dimension[1], dimension[2], room[2])
            bedroom_manager.add_bedroom(bedroom)

            # Pass the room tuple (name, size) to furniture
            handler = FurnitureUI(bedroom)
            handlers.append(handler)

        user_manager.show_users()

        # MUST start the mainloop at the end to ensure all the TopLevel are created
        for handler in handlers:
            handler.start_mainloop()


class BedRoomUI(tk.Frame):
    def __init__(self, parent, user):
        super().__init__(parent)

        max_rooms = 3
        entries = []    # A list of LabelEntry. Each room has a name and size, so 2 entries per room
        fields = ["Room name", "Room size (LxWxH in inches)", "Free space percentage"]

        for room in range(1, max_rooms+1):
            Label(parent, "BedRoom"+str(room))
            for field in fields:
                entries.append(LabelEntry(parent, field, width=30))

        ControlButton(parent, entries, max_rooms, user)
