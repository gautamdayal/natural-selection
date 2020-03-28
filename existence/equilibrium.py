from matplotlib import pyplot as plt
from matplotlib import animation
import random

# A class of species that cannot reproduce
# Population is entirely driven by birth and death rates
class Existor(object):
    def __init__(self, population, birth_rate, death_rate):
        self.population = population
        self.birth_rate = birth_rate
        self.death_rate = death_rate

    def update(self):
        if random.randint(0, 100) < self.birth_rate:
            self.population += 1
        for organism in range(self.population):
            if random.randint(0, 100) < self.death_rate:
                self.population -= 1

    def getEquilibrium(self):
        return(self.birth_rate/self.death_rate)

# A more realistic version of the Species class as organisms can replicate
class Replicator(Existor):
    def __init__(self, population, birth_rate, death_rate, replication_rate):
        Existor.__init__(self, population, birth_rate, death_rate)
        self.replication_rate = replication_rate

    def update(self):
        Existor.update(self)
        for organism in range(self.population):
            if random.randint(0, 100) < self.replication_rate:
                self.population += 1

    def getEquilibrium(self):
        return(self.birth_rate/(self.death_rate - self.replication_rate))

raindrop = Existor(0, 100, 10)
pigeon = Replicator(3, 10, 5, 3)

fig = plt.figure()
ax = plt.axes()
population, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    m = 0.05
    y = x * m + 0.1
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=100, blit=True)

plt.show()
