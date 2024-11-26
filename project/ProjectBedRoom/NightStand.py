from Furniture import Furniture

class NightStand(Furniture):
    def __init__(self):
        self.night_stand_size = "s"
        self.night_stands = {
            "s": (18,14,24),
            "m": (18,14,24),
            "l": (18,14,24)  # unfinish
        }

    def calculateArea(self):
        return super().calculateArea()

    def getUserInput(self, name):
        while True:
            self.night_stand_size = input("Choose night stand table type (s, m, l): ").lower()
            if self.validateUserInput(name):
                break

    def validateUserInput(self, name):
        if self.night_stand_size not in self.night_stands:
            print(f"ERROR - Invalid night stand type: {self.night_stand_size}")
            return False
        else:
            width, length, height = self.night_stands[self.night_stand_size]
            super().setProperties(width, length, height, name, self.night_stand_size)
            return True