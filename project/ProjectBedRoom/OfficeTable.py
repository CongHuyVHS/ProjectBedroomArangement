from Furniture import Furniture

class OfficeTable(Furniture):
    def __init__(self):
        self.office_table_size = "s"
        self.office_tables = {
            "s": (40,20,28),
            "m": (48,24,28),
            "l": (60,30,28)
        }

    def calculateArea(self):
        return super().calculateArea()

    def getUserInput(self, name):
        while True:
            self.office_table_size = input("Choose office table type (s, m, l): ").lower()
            if self.validateUserInput(name):
                break

    def validateUserInput(self, name):
        if self.office_table_size not in self.office_tables:
            print(f"ERROR - Invalid office table type: {self.office_table_size}")
            return False
        else:
            width, length, height = self.office_tables[self.office_table_size]
            super().setProperties(width, length, height, name, self.office_table_size)
            return True
