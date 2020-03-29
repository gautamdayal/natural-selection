from matplotlib import pyplot as plt
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

    def plotPopulation(self, cycles, with_equilibrium = False):
        X = [i for i in range(cycles)]
        Y = []
        for cycle in range(cycles):
            self.update()
            Y.append(self.population)

        plt.plot(X, Y)
        if with_equilibrium:
            plt.plot([self.getEquilibrium() for i in range(cycles)])
        plt.show()

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

# raindrop.plotPopulation(500, True)
pigeon.plotPopulation(500, True)
