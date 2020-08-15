import queue
class animal:
    """Class to manage the animal in the simulation"""
    def __init__(self, x, y, range, speed):
        self.x = x
        self.y = y
        self.range = range
        self.speed = speed
        self.hunger = 100
        self.food_near = []

    def find_food(self, board):
        self.food_near = []
        x_area = range(self.x - int(self.range), self.x + int(self.range))
        y_area = range(self.y - int(self.range), self.y + int(self.range))
        area = [x_area, y_area]
        for x in x_area:
            for y in y_area:
                if board[x][y] == 1:
                    self.food_near.append((x, y))
        return self.food_near

    def end_found(self, moves, x, y, foodx, foody):
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            elif move == "R":
                x += 1
        if x == foodx and y == foody:
            return True
        else:
            return False

    def valid_path(self, moves, x, y):
        for move in moves:
            if move == "U":
                y += 1
            elif move == "D":
                y -= 1
            elif move == "L":
                x -= 1
            elif move == "R":
                x += 1
        if x < 100 and x > 0 and y < 100 and y > 0:
            return True
        else:
            return False


    def find_best_path(self, foodx, foody):
        q = queue.Queue()
        q.put("")
        put = ""
        add = ""
        while True:
            add = q.get()
            for i in ["L", "R", "U", "D"]:
                put = add + i
                if self.valid_path(put, self.x, self.y):
                    q.put(put)
            if self.end_found(put, self.x, self.y, foodx, foody):
                break
        return q.get()


if __name__ == '__main__':
    a = animal(5, 5, 5, 5)
    a.find_food()
    #print(a.find_best_path(7, 7))
