from Furniture import Furniture

class Drawer(Furniture):
    def __init__(self,name,type):

        self.name = name
        self.drawerType = type
        self.drawerSizes={
            "3 drawers": (30,18,30),
            "4 drawers": (36,18,42),
        }
        width, length, height = self.drawerSizes[self.drawerType]
        super().setProperties(width, length, height, name, self.drawerType)

    def calculateArea(self):
        return super().calculateArea()

    def show_drawer(self):
        print(f"Drawer name: {self.name}, type: {self.drawerType}")


    # def getUserInput(self, name):
    #     while True:
    #         self.drawerSize = input("Choose drawer type (3 or 4): ")
    #         if self.validateUserInput(name):
    #             break
    #
    # def validateUserInput(self, name):
    #     if self.drawerSize not in self.drawers:
    #         print(f"ERROR - Invalid drawer type: {self.drawerSize}")
    #         return False
    #     else:
    #         width, length, height = self.drawers[self.drawerSize]
    #         super().setProperties(width, length, height, name, self.drawerSize)
    #         return True
