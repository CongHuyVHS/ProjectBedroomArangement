from BedRoom import BedRoom

class BedRoomManager():
    def __init__(self):
        self.bedrooms = []

    def arrange_room(self):
        # room = BedRoom(room_name)
        # room.getUserInput()
        # room.displayUserInput()
        # room.arangeRoom()
        pass

    def add_bedroom(self, bedroom):
        self.bedrooms.append(bedroom)

    def show_bedrooms(self):
        for bedroom in self.bedrooms:
            bedroom.show_bedroom()