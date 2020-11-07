import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

import numpy as np

from Sim import sim
import random

"""
EX
{'cycle': 67, 'pop': 0, 'animals': {'speed': [], 'range': []}}
"""
class graphs:
    """Class to manage graphing the simulation"""
    def __init__(self):
        self.cycles = 100
        self.sim = sim(15, self.cycles)
        print ("Running the simulation...")
        self.sim.run()
        print ("Simulation finished")
        self.data = self.sim.datasets
        self.data.pop()

    def plot_animal_attributes(self):
        """
        Plot animal attributes
        """
        self.animal_fig, self.animal_ax = plt.subplots(figsize=(5, 5))
        self.animal_ax.set_xlabel("Speed")
        self.animal_ax.set_ylabel("Range")
        self.animal_ax.set_xlim(-1, 11)
        self.animal_ax.set_ylim(-1, 11)
        #Append speed and range to arrays above in animate functions
        #Ex: https://stackoverflow.com/questions/42722691/python-matplotlib-update-scatter-plot-from-a-function
        x_data = []
        y_data = []
        sizes = []

        scatter = self.animal_ax.scatter(0, 0, c="#ffffff")

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
            scatter = self.animal_ax.scatter(x_data, y_data, s=sizes, c="#ff0000")
            try:
                scatter.set_offsets(points)
            except ValueError:
                pass
            return scatter,

        line_animation = animation.FuncAnimation(
            self.animal_fig, animate, frames=np.arange(0, len(self.data), 1), interval=0.05*1000,
            blit=True, save_count=len(self.data)
        )

        writergif = animation.PillowWriter(fps=15)
        line_animation.save('graph.gif',writer=writergif)
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
            cycles.append(cycles[-1]+1)

        self.pop_ax.plot(cycles, populations)

        self.pop_fig.savefig("population.png")
        plt.close(self.pop_fig)


    # def test(self):
    #     fig, ax = plt.subplots()
    #     ax.set_xlabel("Speed")
    #     ax.set_ylabel("Range")
    #     ax.set_xlim(0, 10)
    #     ax.set_ylim(0, 10)
    #
    #     x_data = []
    #     y_data = []
    #     scatter = ax.scatter(0, 0)
    #
    #     def create_coordinates(x, y):
    #         points = []
    #         for n, x_coor in enumerate(x):
    #             coor = (x_coor, y[n])
    #             points.append(coor)
    #         return points
    #
    #     def animate(i):
    #         x_data = [random.randint(1, 10) for i in range(5)]
    #         y_data = [random.randint(1, 10) for i in range(5)]
    #         points = create_coordinates(x_data, y_data)
    #         scatter.set_offsets(points)
    #         return scatter,
    #
    #     ani = animation.FuncAnimation(fig, func=animate, frames=np.arange(0, 10, 0.1), interval=10)
    #     plt.show()

if __name__ == '__main__':
    g = graphs()
    g.plot_animal_attributes()
    g.plot_population()
