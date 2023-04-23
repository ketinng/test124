from wheel import Wheel
class Brake(Wheel):
    title:str

    def __init__(self,title):
        self.title = title
    def apply(self):
        pass