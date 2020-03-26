# import matplotlib.pyplot as plt
import random

class Species(object):
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

pigeon = Species(0, 100, 10)

n = 100
for i in range(n):
    print(pigeon.population)
    pigeon.update()
