from tire import Tyre
class Wheel(Tyre):
    diameter: float
    size: int

    def __init__(self,diameter,size):
        self.diameter = diameter
        self.size = size