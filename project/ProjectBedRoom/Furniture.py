class Furniture:
    def __init__(self):
        self.width = self.length = self.height = self.area = 0
        self.name = ""
        self.type = ""
    def calculateArea(self):
        self.area =  self.width*self.length
        return self.area

    def getUserInput(self, name):
        raise NotImplementedError

    def validateUserInput(self, name):
        raise NotImplementedError

    def add_furniture(self):
        raise NotImplementedError

    def delete_furniture(self):
        raise NotImplementedError

    def setProperties(self ,width, length, height, name, type):
        self.width = width
        self.height = height
        self.length = length
        self.name = name
        self.type = type
        self.calculateArea()

    def displayInput(self):
        print("name: ",self.name, ", type: ", self.type, ", width(in inches): ", self.width, ", height(in inches): ",
              self.height, ", length(in inches): ", self.length, ", area: ", self.area)
