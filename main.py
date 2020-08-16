from Food import food
from Animal import animal
from Graphs import graphs
import numpy as np
import random
import queue

class sim:
    """Class to run the simulation"""
    def __init__(self):
        self.WIDTH = 100
        self.HEIGHT = 100
        self.cycles = 0
        self.population = 0
        self.animals = []
        self.range = 5
        self.speed = 5
        self.board = np.zeros((self.WIDTH, self.HEIGHT), dtype=int)
        self.foods = []
        self.REPETITIONS = 100
        self.cycles = 0

    def create_food(self, range):
        self.foods = []
        restricted_spots = {}
        for i in range:
            for food_item in self.foods:
                restricted_spots[food_item.x] = food_item.y
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
            self.animals.append(animal(x, y, self.range, self.speed))

    def run(self):
        self.create_initial_population(range(50))
        while self.cycles < self.REPETITIONS:
            self.board = np.zeros((self.WIDTH, self.HEIGHT), dtype=int)
            food_needed = range(100 - len(self.foods))
            self.create_food(food_needed)
            for food in self.foods:
                self.board[food.x][food.y] = 1
            food = 0
            for j in self.board:
                for i in j:
                    if i == 1:
                        food += 1
            for animal in self.animals:
                if animal.searching_for_food:
                    animal.find_food(self.board)
            self.cycles += 1

if __name__ == '__main__':
    s = sim()
    s.run()
