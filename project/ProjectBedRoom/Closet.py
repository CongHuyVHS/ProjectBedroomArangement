from Furniture import Furniture

class Closet(Furniture):

    def __init__(self):
        self.closetSize = "default"
        self.closets = {
            "s": (24,72,24),
            "m": (36,72,24),
            "l": (48,72,24)
        }

    def calculateArea(self):
        return super().calculateArea()

    def getUserInput(self, name):
        while True:
            self.closetSize = input("Choose closet type (s, m, l): ").lower()
            if self.validateUserInput(name):
                break

    def validateUserInput(self, name):
        if self.closetSize not in self.closets:
            print(f"ERROR - Invalid closet type: {self.closetSize}")
            return False
        else:
            width,length,height = self.closets[self.closetSize]
            super().setProperties(width,length,height,name,self.closetSize)
            return True
