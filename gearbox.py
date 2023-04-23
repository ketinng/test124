from gearboxtype import Gearboxtype

class Gearbox(Gearboxtype):
    gearRatio: float
    currentGear: int
    def __init__(self, gearRatio: float, currentGear:int):
        self.gearRatio = gearRatio
        self.currentGear = currentGear
    def shiftup(self):
        print("Change gear")
    def shiftdown(self):
        print("Change gear")