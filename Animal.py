class animal:
    """Class to manage the animal in the simulation"""
    def __init__(self, x, y, range, speed):
        self.x = x
        self.y = y
        self.range = range
        self.speed = speed
        self.hunger = 100

if __name__ == '__main__':
    a = animal()
