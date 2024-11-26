from Drawer import  Drawer
from Factory import FurnitureFactory


class DrawerFactory(FurnitureFactory):
    def __init__(self):
        self.drawers = {}
        self.total_area = 0

    def add_furniture(self, drawer,name):
        self.drawers[name] = drawer

    def delete_furniture(self, name):
        del self.drawers[name]

    def calculateTotalArea(self):
        for drawer in self.drawers.values():
            self.total_area += drawer.calculateArea()
        return self.total_area

    def show_furniture(self):
        for key, value in self.drawers.items():
            value.show_drawer()

    def clear_furniture(self):
        self.drawers.clear()

    # def getUserInput(self):
    #     while True:
    #         try:
    #             num_drawer = int(input("How many drawer would you like to have?: "))
    #             if num_drawer < 0:
    #                 print("please enter a positive number")
    #             else:
    #                 break
    #         except ValueError:
    #             print("Please enter a number")
    #
    #     for i in range(1,num_drawer+1):
    #         drawer = Drawer()
    #         drawer_name = "drawer"+str(i)
    #         drawer.getUserInput(drawer_name)
    #         self.addFurniture(drawer,drawer_name)
    #
    # def displayUserInput(self):
    #     for key, value in self.drawers.items():
    #         print(f"drawers name: {key}")
    #         value.displayInput()

