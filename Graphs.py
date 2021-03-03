import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

import numpy as np

from Sim import sim
import random

import json

"""
EX
{'cycle': 67, 'pop': 0, 'animals': {'speed': [], 'range': []}}
"""
class graphs:
    """Class to manage graphing the simulation"""
    def __init__(self):
        self.cycles = 100
        print ("Retrieving simulation data...")
        with open('data.json') as f:
            data = json.load(f)
        self.data = data[:-1]
        self.data.pop()

    def plot_animal_attributes(self):
        """
        Plot animal attributes
        """

        #Create graph
        self.animal_fig, self.animal_ax = plt.subplots(figsize=(5, 5))

        #Set labels and axis for graph
        self.animal_ax.set_xlabel("Speed")
        self.animal_ax.set_ylabel("Range")
        self.animal_ax.set_xlim(-1, 11)
        self.animal_ax.set_ylim(-1, 11)

        x_data = []
        y_data = []
        sizes = []

        scatter = self.animal_ax.scatter(-2, -2, c="#ff0000")

        #Create (x, y) coordinates
        def create_coordinates(x, y):
            coordinates = []
            for n, x_coor in enumerate(x):
                coor = (x_coor, y[n])
                coordinates.append(coor)
            return coordinates

        #Create sizes for points
        def create_sizes(coordinates):
            sizes = []
            for point in coordinates:
                size = coordinates.count(point) * 80
                sizes.append(size)
            return sizes

        def animate(i):
            data = self.data[i]
            x_data = data["animals"]["speed"]
            y_data = data["animals"]["range"]
            plt.title(f"Cycle: {data['cycle']}      Population: {data['pop']}")
            points = create_coordinates(x_data, y_data)
            sizes = create_sizes(points)

            #Update the graph
            scatter.set_offsets(points)
            scatter.set_sizes(sizes)
            return scatter,

        line_animation = animation.FuncAnimation(
            self.animal_fig, animate, frames=np.arange(0, len(self.data), 1), interval=0.05*1000,
            blit=True, save_count=len(self.data)
        )

        writergif = animation.PillowWriter(fps=5)
        line_animation.save('animals.gif',writer=writergif)
        plt.close(self.animal_fig)

    def plot_population(self):
        self.pop_fig, self.pop_ax = plt.subplots(figsize=(5, 5))
        self.pop_ax.set_xlabel("Cycle")
        self.pop_ax.set_ylabel("Population")
        populations, cycles = [], []
        for dataset in self.data:
            populations.append(dataset['pop'])
            cycles.append(dataset['cycle'])

        """
        If the simulation ended when all the animals died,
        Add zero to the population
        """
        if cycles[-1] + 1 < self.cycles:
            populations.append(0)
            cycles.append(cycles[-1] + 1)

        self.pop_ax.plot(cycles, populations)

        #Create the average line
        y_average = 0
        for i in populations:
            y_average += i
        y_average = y_average / len(populations)
        y_average = [y_average] * len(populations)

        x_values = np.arange(0, len(populations), 1)
        self.pop_ax.plot(x_values, y_average, label='Mean', linestyle='--')

        self.pop_fig.savefig("population.png")
        plt.close(self.pop_fig)


if __name__ == '__main__':
    g = graphs()
    g.plot_animal_attributes()
    g.plot_population()
