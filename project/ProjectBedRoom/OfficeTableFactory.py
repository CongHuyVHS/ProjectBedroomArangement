from OfficeTable import OfficeTable
from Factory import FurnitureFactory 

class OfficeTableFactory(FurnitureFactory):
    def __init__(self):
        self.office_tables = {}
        self.total_area = 0
    def addFurniture(self, office_table,name):
        self.office_tables[name] = office_table
    def deleteFurniture(self, name):
        del self.office_tables[name]
    def getUserInput(self):
        while True:
            try:
                num_office_table = int(input("How many office_table would you like to have?: "))
                if num_office_table < 0:
                    print("please enter a positive number")
                else:
                    break
            except ValueError:
                print("Please enter a number")

        for i in range(1,num_office_table+1):
            office_table = OfficeTable()
            office_table_name = "officetable"+str(i)
            office_table.getUserInput(office_table_name)
            self.addFurniture(office_table,office_table_name)

    def displayUserInput(self):
        for key, value in self.office_tables.items():
            print(f"office table name: {key}")
            value.displayInput()
    def calculateTotalArea(self):
        for office_table in self.office_tables.values():
            self.total_area += office_table.calculateArea()
        return self.total_area

