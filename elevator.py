class Elevator:
    def __init__(self, id , total):
        self.id = id
        self.current = 0
        self.total = total
    def go_to(self, floor):
        if 0<= floor<= self.total:
            self.current = floor
            print("Elevator reached to", floor)
            return True
        else:
            print("Elevator can only go to floor 0 to", self.total)
            return False
            
ele1= Elevator(1, 6)
ele2= Elevator(2, 5)
ele1.go_to(3)
ele1.go_to(-1)
ele2.go_to(7)
ele2.go_to(3)
