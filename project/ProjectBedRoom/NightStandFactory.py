from NightStand import NightStand
from Factory import FurnitureFactory

class NightStandFactory(FurnitureFactory):
    def __init__(self):
        self.nightStands = {}
        self.total_area = 0

    def addFurniture(self, nightStand, name):
        self.nightStands[name] = nightStand

    def deleteFurniture(self, name):
        del self.nightStands[name]

    def getUserInput(self):
        while True:
            try:
                num_nightStand = int(input("How many night stand would you like to have?: "))
                if num_nightStand < 0:
                    print("please enter a positive number")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        for i in range(1,num_nightStand+1):
            night_stand = NightStand()
            night_stand_name = "nightstand"+str(i)
            night_stand.getUserInput(night_stand_name)
            self.addFurniture(night_stand,night_stand_name)

    def displayUserInput(self):
        for key, value in self.nightStands.items():
            print(f"night stand name: {key}")
            value.displayInput()

    def calculateTotalArea(self):
        for nightStand in self.nightStands.values():
            self.total_area += nightStand.calculateArea()
        return self.total_area

