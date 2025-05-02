class Vehicle:
    def __init__(self, license_plate):
        self.license_plate = license_plate

class Car(Vehicle): pass
class Truck(Vehicle): pass
class Motorcycle(Vehicle): pass

class ParkingSlot:
    def __init__(self, slot_id, size):
        self.slot_id = slot_id
        self.size = size
        self.occupied_by = None

    def is_available(self):
        return self.occupied_by is None

    def park(self, vehicle):
        if self.is_available():
            self.occupied_by = vehicle
            return True
        return False

    def leave(self):
        self.occupied_by = None
