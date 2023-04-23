from wheel import Wheel
class Suspension(Wheel):
    springRate:float

    def __init__(self,springRate):
        self.springRate = springRate