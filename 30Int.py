# class Tuna:
#     def __init__(self):
#         print("the initial function")
#
#     def swim(self):
#         print("I am swimming")
#
# flipper = Tuna()
# flipper.swim()

class Enemy:
    def __init__(self, x):
        self.energy = x
        print("initialize the class", self.energy)
    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)
jason.get_energy()
sandy.get_energy()