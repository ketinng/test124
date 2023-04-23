from gearbox import Gearbox
from carmodel import Carmodel
from body import Body
from engine import Engine
from brakes import Brake
from suspension import Suspension


class bmw(Gearbox,Carmodel,Body,Engine,Brake,Suspension):

    def __init__(self, registrationNum : str, year:int, licensenumber: str,):
        self.registrationNum = registrationNum
        self.year = year
        self.licensenumber = licensenumber

    def moveforward(self):
        print("gas")
    def movebackward(self):
        print("reverse and then gas")
    def stop(self):
        print("hit the brakes")
    def turnLeft(self):
        print("the wheel goes left")
    def turnRight(self):
        print("the wheel goes right")