class food:
    """Class to manage the food in the simulation"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = 'normal'


if __name__ == '__main__':
    f = food(1, 1)
    print (f.type)
