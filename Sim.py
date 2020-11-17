from Food import food
from Animal import animal
import numpy as np
import random
from Nqueue import nqueue

import json

class sim:
    """Class to run the simulation"""
    def __init__(self, pop, reps):
        self.WIDTH = 20
        self.HEIGHT = 20
        self.REPETITIONS = reps
        self.initial_pop = pop
        self.cycles = 0
        self.population = 0
        self.animals = []
        self.board = np.zeros((self.WIDTH, self.HEIGHT), dtype=int)
        self.foods = []
        self.cycles = 0
        self.restricted_spots = {}
        self.datasets = []
        self.food_amount = 100

    def create_food(self, range):
        print ("creating food")
        restricted_spots = {}
        for i in range:
            for food_item in self.foods:
                restricted_spots[food_item.x] = food_item.y

            for animal in self.animals:
                restricted_spots[animal.x] = animal.y
            x = random.randint(0, self.WIDTH - 2)
            y = random.randint(0, self.HEIGHT - 2)
            for j in restricted_spots:
                if x == j:
                    x += 1
                if y == restricted_spots[j]:
                    y += 1
                if x > self.WIDTH - 1:
                    x = 1
                if y > self.HEIGHT - 1:
                    y = 1
            self.foods.append(food(x, y))
        print ("done")

    def create_initial_population(self, pop):
        restricted_spots = {}
        for i in pop:
            x = random.randint(0, self.WIDTH - 1)
            y = random.randint(0, self.HEIGHT - 1)
            for j in restricted_spots:
                if x == j:
                    x += 1
                if y == restricted_spots[j]:
                    y += 1
            restricted_spots[x] = y
            speed = random.randint(1, 10)
            range = random.randint(5, 10)
            self.animals.append(animal(x, y, range, speed))

    def get_restricted_spots(self):
        self.restricted_spots = {}
        for food_item in self.foods:
            self.restricted_spots[food_item.x] = food_item.y

        for animal in self.animals:
            self.restricted_spots[animal.x] = animal.y

    def run(self):
        #Create initial assets for simulation
        self.create_initial_population(range(self.initial_pop))
        self.create_food(range(self.food_amount))

        while self.cycles < self.REPETITIONS:
            print (f"📘📘📘Population: {len(self.animals)}")
            print (f"📘📘📘Food: {len(self.foods)}")

            #If there are no more animals
            if len(self.animals) < 1:
                break

            ####################Create the board###########################
            self.board = np.zeros((self.WIDTH, self.HEIGHT), dtype=int)
            if len(self.foods) < self.food_amount - 10:
                food_needed = range(self.food_amount - 1 - len(self.foods))
                self.create_food(food_needed)
                for food in self.foods:
                    self.board[food.x][food.y] = 1

                #Get animals to find new food when food is added
                new_animal_array = []
                for animal in self.animals:
                    if not animal.food_near:
                        animal.find_food(self.board)
            for food in self.foods:
                self.board[food.x][food.y] = 1
            food = 0


            new_animal_array = []
            ###Using the animals###
            for animal in self.animals:
                ###Find food###
                if animal.searching_for_food:
                    print ("📔📔📔Searching for food")
                    animal.find_food(self.board)
                    if animal.food_near != []:
                        animal.find_best_path(animal.food_near[0], animal.food_near[1])
                    else:
                        animal.move_queue = nqueue()
                        for i in range(animal.speed):
                            animal.move_queue.add(random.choice(["L", "R", "U", "D"]))
                        animal.searching_for_food = True
                        animal.move_to_food()
                else:
                    if animal.move_queue.get_q() == []:
                        animal.searching_for_food = True

                    #Get method to return index for food, then pop in main.py
                    self.foods, animal.searching_for_food = animal.eat(self.foods)
                    animal.move_to_food()

                if animal.hunger > 20:
                    animal.hunger = 10
                    self.get_restricted_spots()
                    new_animals = animal.reproduce(self.restricted_spots, self.WIDTH, len(self.animals))
                    print ("reproduce")

                    for new_animal in new_animals:
                        new_animal.find_food(self.board)
                        new_animal_array.append(new_animal)

                animal.hunger -= 1
                new_animal_array.append(animal)
                if animal.hunger <= 0:
                    print (f"📕📕📕Rip {animal}")
                    new_animal_array.pop(new_animal_array.index(animal))
            ############################################################################
            self.animals = new_animal_array
            self.cycles += 1
            print (self.cycles)

            data = {}
            animals_data = {}
            animals_data["speed"] = []
            animals_data["range"] = []
            animals_data["info"] = []

            for animal in self.animals:
                animals_data["speed"].append(animal.speed)
                animals_data["range"].append(animal.animal_range)

                animal_info = {
                    "x": animal.x,
                    "y": animal.y,
                    "hunger": animal.hunger
                }
                animals_data["info"].append(animal_info)

            food_data = []
            for food in self.foods:
                food = {
                    "x": food.x,
                    "y": food.y
                }
                food_data.append(food)

            data["cycle"] = self.cycles
            data["pop"] = len(self.animals)
            data["animals"] = animals_data
            data["food_data"] = food_data

            self.datasets.append(data)


if __name__ == '__main__':
    s = sim(20, 200)
    s.run()
    for data in s.datasets:
        print (data)
    with open("data.json", "w") as f:
        json.dump(s.datasets, f)
