from operator import length_hint

from BedFactory import BedFactory
from ClosetFactory import ClosetFactory
from DrawerFactory import DrawerFactory
from NightStandFactory import NightStandFactory
from OfficeTableFactory import OfficeTableFactory


class BedRoom:
    def __init__(self, name, length, width, height, free_space):
        self.name = name
        self.furnitures = []
        self.width = width
        self.length = length
        self.height = height
        self.area = 0
        self.freeSpacePercent = free_space
        self.furniture_area = 0

    def calculate_room_area(self):
        self.area = self.width * self.height

    def show_bedroom(self):
        print(f"Bedroom name: {self.name}, width: {self.width}, length: {self.length}, height: {self.height}, free space: {self.freeSpacePercent}")

    def set_furniture(self):
        bed_factory = BedFactory()
        self.furnitures.append(bed_factory)

        closet_factory = ClosetFactory()
        self.furnitures.append(closet_factory)

        drawer_factory = DrawerFactory()
        self.furnitures.append(drawer_factory)

        night_stand_factory = NightStandFactory()
        self.furnitures.append(night_stand_factory)

        office_table_factory = OfficeTableFactory()
        self.furnitures.append(office_table_factory)

    def arrange_room(self):
        self.calculate_room_area()

        # Calculate all furniture areas
        for furniture in self.furnitures:
                self.furniture_area += furniture.calculateTotalArea()

        free_area = self.area - self.furniture_area
        if free_area <= 0:
            print(f"FINAL RESULT - Not enough space for all furniture")
        else:
            if free_area * 100 /self.area < self.freeSpacePercent:
                print(f"FINAL RESULT - All furniture can fit in the room however the room free space (default 20%) is not respected")
            else:
                print(f"FINAL RESULT - All furniture can fit in the room.Free space area remaining(in inches): {free_area} ")

