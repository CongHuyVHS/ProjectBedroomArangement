from Closet import Closet
from Factory import FurnitureFactory

class ClosetFactory(FurnitureFactory):
    def __init__(self):
        self.closets = {}
        self.total_area = 0

    def addFurniture(self, closet, name):
        self.closets[name] = closet

    def deleteFurniture(self, name):
        del self.closets[name]

    def getUserInput(self):
        while True:
            try:
                num_closet = int(input("How many closet would you like to have?: "))
                if num_closet < 0:
                    print("please enter a positive number")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        for i in range(1,num_closet+1):
            closet = Closet()
            closet_name = "closet"+str(i)
            closet.getUserInput(closet_name)
            self.addFurniture(closet, closet_name)

    def displayUserInput(self):
        for key, value in self.closets.items():
            print(f"closet name: {key}")
            value.displayInput()

    def calculateTotalArea(self):
        for closet in self.closets.values():
            self.total_area += closet.calculateArea()
        return self.total_area

