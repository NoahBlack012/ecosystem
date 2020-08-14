from Food import food
from Animal import animal
from Graphs import graphs

class sim:
    """Class to run the simulation"""
    def __init__(self):
        self.food = food()
        self.animal = animal()

    def run(self):
        pass

if __name__ == '__main__':
    s = sim()
    sim.run()