from Furniture import Furniture


class Bed(Furniture):
    def __init__(self, name, type):

        self.name = name
        self.bedType = type
        self.bedSizes = {
            "king": (76, 80, 14),
            "queen": (60, 80, 14),
            "double": (54, 75, 14),
            "single": (38, 75, 14),
        }

        width, length, height = self.bedSizes[self.bedType]
        super().setProperties(width, length, height, name, self.bedType)

    def calculateArea(self):
        return super().calculateArea()

    def show_bed(self):
        print(f"Bed name: {self.name}, type: {self.bedType}")

