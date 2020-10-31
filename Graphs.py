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
        self.fig, self.ax = plt.subplots(figsize=(5, 5))
        self.ax.set_xlabel("Speed")
        self.ax.set_ylabel("Range")
        self.ax.set_xlim(1, 11)
        self.ax.set_ylim(1, 11)
        self.sim = sim(10, 100)
        print ("Running the simulation...")
        self.sim.run()
        print ("Simulation finished")
        self.data = self.sim.datasets
        self.data.pop()

    def plot(self):
        """
        Plot the graphs
        """
        #Append speed and range to arrays above in animate functions
        #Ex: https://stackoverflow.com/questions/42722691/python-matplotlib-update-scatter-plot-from-a-function
        x_data = []
        y_data = []
        scatter = self.ax.scatter(0, 0)
        def create_coordinates(x, y):
            points = []
            for n, x_coor in enumerate(x):
                coor = (x_coor, y[n])
                points.append(coor)
            return points

        def animate(i):
            data = self.data[i]
            x_data = data["animals"]["speed"]
            y_data = data["animals"]["range"]
            plt.title(f"Cycle: {data['cycle']}      Population: {data['pop']}")
            points = create_coordinates(x_data, y_data)
            try:
                scatter.set_offsets(points)
            except ValueError:
                pass
            return scatter,

        line_animation = animation.FuncAnimation(
            self.fig, animate, frames=np.arange(0, len(self.data), 1), interval=0.1*1000,
            blit=True, save_count=len(self.data)
        )

        writergif = animation.PillowWriter(fps=1)
        line_animation.save('graph.gif',writer=writergif)

        plt.show()

    def test(self):
        fig, ax = plt.subplots()
        ax.set_xlabel("Speed")
        ax.set_ylabel("Range")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)

        x_data = []
        y_data = []
        scatter = ax.scatter(0, 0)

        def create_coordinates(x, y):
            points = []
            for n, x_coor in enumerate(x):
                coor = (x_coor, y[n])
                points.append(coor)
            return points

        def animate(i):
            x_data = [random.randint(1, 10) for i in range(5)]
            y_data = [random.randint(1, 10) for i in range(5)]
            points = create_coordinates(x_data, y_data)
            scatter.set_offsets(points)
            return scatter,

        ani = animation.FuncAnimation(fig, func=animate, frames=np.arange(0, 10, 0.1), interval=10)
        plt.show()

if __name__ == '__main__':
    g = graphs()
    g.plot()
