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
        self.move_queue = nqueue()
        self.moves = ""

    def move_to_food(self):
        #Boolean for determining if animal has found any food
        has_path = False
        if self.move_queue:
            #If the animal has a queue, they have found a food
            has_path = True

        moved = 0
        for i in range(self.speed):
            empty_queue = False
            moves = self.move_queue.de_q()
            try:
                new_q = moves[1:]
            except TypeError as e:
                if not has_path:
                    self.searching_for_food = True
            try:
                try:
                    move = moves[0]
                except TypeError as t:
                    empty_queue = True
            except IndexError as e:
                empty_queue = True

            if empty_queue:
                """
                If the animal has a path set, an empty queue means
                they have reached their food and should exit
                """
                if has_path:
                    break

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

    def reproduce(self, restricted_spots, length, population):
        x_interval = 1
        y_interval = 0
        while True:
            new_x = self.x + x_interval
            new_y = self.y + y_interval
            if new_x > length:
                new_x = 1
            if new_y > length:
                new_y = 1
            try:
                if restricted_spots[new_x] != new_y:
                    break
            except KeyError as e:
                break
            if x_interval % 2 == 0:
                x_interval += 1
            else:
                y_interval += 1
        if population > 10:
            mutation_chance = 50
        elif population < 7 and population > 3:
            mutation_chance = 20
        else:
            mutation_chance = 5
        speed_rand = random.randint(1, mutation_chance)
        if speed_rand == 1:
            speed = random.randint(1, 5)
        else:
            speed = self.speed

        range_rand = random.randint(1, mutation_chance)
        if range_rand == 1:
            range = random.randint(5, 10)
        else:
            range = self.range
        new_animal = animal(new_x, new_y, range, speed)
        return new_animal

    def eat(self, foods):
        x, y = -1, -1
        for food in foods:
            if food.x == self.x and food.y == self.y:
                print (f"📗📗📗{self} yum x: {self.x} y:{self.y}")
                self.searching_for_food = True
                self.hunger += 10
                x = food.x
                y = food.y
                self.food_near = []
                self.move_queue = nqueue()
                break
        new_foods = []
        for food in foods:
            if food.x != x or food.y != y:#Fix to error where too much food gets removed
                new_foods.append(food)

        return new_foods, self.searching_for_food

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
            if comps > 30000:
                break
        q = q.get_q()[0]
        new_q = nqueue()
        new_q.add(q)
        self.move_queue = new_q


if __name__ == '__main__':
    a = animal(5, 5, 5, 5)
    a.find_food()
    #print(a.find_best_path(7, 7))
