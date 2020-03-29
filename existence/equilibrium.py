from matplotlib import pyplot as plt
import random

# A class of species that cannot reproduce
# Population is entirely driven by birth and death rates
class Existor(object):
    def __init__(self, population, birth_rate, death_rate):
        self.population = population
        self.birth_rate = birth_rate
        self.death_rate = death_rate

    # Updates population based on birth and death rates
    def update(self):
        if random.randint(0, 100) < self.birth_rate:
            self.population += 1
        for organism in range(self.population):
            if random.randint(0, 100) < self.death_rate:
                self.population -= 1

    # Returns the predicted equilibrium value based on our equation
    def getEquilibrium(self):
        return(self.birth_rate/self.death_rate)

    # Takes three arguments: number of cycles, whether to plot equilibrium, whether to plot mean
    def plotPopulation(self, cycles, with_equilibrium = False, with_mean = False):
        Y = []
        for cycle in range(cycles):
            self.update()
            Y.append(self.population)

        plt.ylim(0, 5 * self.getEquilibrium())
        plt.plot(Y, label='Population')

        if with_mean:
            mean = sum(Y)/len(Y)
            plt.plot([mean for i in range(cycles)], label = 'Mean population')

        if with_equilibrium:
            plt.plot([self.getEquilibrium() for i in range(cycles)], label = 'Predicted equilibrium')
        plt.xlabel('Cycles')
        plt.ylabel('Number of organisms')
        plt.legend()
        plt.show()

# A more realistic child class of Species as organisms can replicate
class Replicator(Existor):
    def __init__(self, population, birth_rate, death_rate, replication_rate):
        Existor.__init__(self, population, birth_rate, death_rate)
        self.replication_rate = replication_rate

    # Inherited from Existor but modified to include a replication rates
    def update(self):
        Existor.update(self)
        for organism in range(self.population):
            if random.randint(0, 100) < self.replication_rate:
                self.population += 1

    def getEquilibrium(self):
        return(self.birth_rate/(self.death_rate - self.replication_rate))

raindrop = Existor(0, 100, 10)
pigeon = Replicator(3, 10, 5, 3)

# raindrop.plotPopulation(500, True, True)
pigeon.plotPopulation(500, True, True)
