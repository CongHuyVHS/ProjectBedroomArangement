from Furniture import Furniture
class FurnitureFactory:
    def __init__(self):
        pass

    def calculateTotalArea(self):
        raise NotImplementedError

    def addFurniture(self,furniture,name):
        raise NotImplementedError

    def deleteFurniture(self,name):
        raise NotImplementedError

    def calculateTotalArea(self):
        raise NotImplementedError

    def show_furniture(self):
        raise NotImplementedError

    def clear_furniture(self):
        raise NotImplementedError