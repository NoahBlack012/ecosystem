import random
class food:
    """Class to manage the food in the simulation"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice([10, 10, 10, 15, 15, 20])

if __name__ == '__main__':
    f = food(1, 1)
    print (f.type)
