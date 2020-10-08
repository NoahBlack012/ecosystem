from Nqueue import nqueue
import random
class animal:
    """Class to manage the animal in the simulation"""
    def __init__(self, x, y, range, speed):
        self.x = x
        self.y = y
        self.range = range
        self.speed = speed
        self.hunger = 10
        self.food_near = []
        self.searching_for_food = True
        self.move_queue = ""
        self.moves = ""

    def move_to_food(self):
        moves = self.move_queue.de_q()
        new_q = moves[1:]
        try:
            move = moves[0]
        except IndexError as e:
            move = random.choice(["U", "D", "L", "R"])
            self.searching_for_food = True
        self.move_queue = nqueue()
        self.move_queue.add(new_q)

        if move == "U":
            self.y += 1
        elif move == "D":
            self.y -= 1
        elif move == "L":
            self.x -= 1
        elif move == "R":
            self.x += 1

    def eat(self, foods):
        x, y = -1, -1
        for food in self.food_near:
            if food[0] == self.x and food[1] == self.y:
                print (f"{self} yum x: {self.x} y:{self.y}")
                self.searching_for_food = True
                self.hunger += 5
                x = food[0]
                y = food[1]
                self.food_near.remove(food)
                break
        new_foods = []
        for food in foods:
            if food.x != x and food.y != y:
                new_foods.append(food)

        return new_foods


    def find_food(self, board):
        self.searching_for_food = False
        x_area = range(self.x - int(self.range), self.x + int(self.range))
        y_area = range(self.y - int(self.range), self.y + int(self.range))
        area = [x_area, y_area]
        for x in x_area:
            for y in y_area:
                try:
                    if board[x][y] == 1:
                        food = [x, y]
                        self.food_near.append(food)
                except IndexError as e:
                    pass

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
        comps = 0
        q = nqueue()
        q.add("")
        put = ""
        add = []
        while True:
            add = q.de_q()
            for i in ["L", "R", "U", "D"]:
                put = add + i
                if self.valid_path(put, self.x, self.y):
                    q.add(put)
            if self.end_found(put, self.x, self.y, foodx, foody):
                break
            comps += 1
            if comps > 20000:
                break
        q = q.get_q()[0]
        new_q = nqueue()
        new_q.add(q)
        self.move_queue = new_q


if __name__ == '__main__':
    a = animal(5, 5, 5, 5)
    a.find_food()
    #print(a.find_best_path(7, 7))
