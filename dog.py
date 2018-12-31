from .agents import *

class BlindDog(Agent):
    def eat(self,thing):
        print("Dog: Ate food at{}.".format(self.location))

    def drink(self,thing):
        print("Dog: Drank water at{}.".format(self.location))


doggo = BlindDog()