from BedroomManager import BedRoomManager
class UserManager():
        def __init__(self):
            self.users = []
            self.bedroom_managers = {}

        def add_user(self, user):
            self.users.append(user)

        def add_bedroom_to_user(self, user, bedroom_manager):
             self.bedroom_managers[user.username] = bedroom_manager

        def show_users(self):
            for key, value in self.bedroom_managers.items():
                print(f"Show bedrooms for user: {key}")
                value.show_bedrooms()