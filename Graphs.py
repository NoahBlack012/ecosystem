import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

from Sim import sim

"""
EX
{'cycle': 67, 'pop': 0, 'animals': {'speed': [], 'range': []}}
"""
class graphs:
    """Class to manage graphing the simulation"""
    def __init__(self):
        self.fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        self.sim = sim()
        sim.run()
        self.data = sim.datasets

    def plot(self):
        def init_func():
            return
        anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

if __name__ == '__main__':
    g = graphs()
