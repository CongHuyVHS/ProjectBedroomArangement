from Bed import Bed
from Factory import FurnitureFactory


class BedFactory(FurnitureFactory):
    def __init__(self):
        self.beds = {}
        self.total_area = 0

    def add_furniture(self, bed, name):
        self.beds[name] = bed

    def delete_furniture(self, name):
        del self.beds[name]

    def calculate_total_area(self):
        for bed in self.beds.values():
            self.total_area += bed.calculateArea()
        return self.total_area

    def show_furniture(self):
        for key, value in self.beds.items():
            value.show_bed()

    def clear_furniture(self):
        self.beds.clear()