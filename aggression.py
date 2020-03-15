import random
import matplotlib.pyplot as plt

doves = 10
hawks = 0

days = 50
lnum = 100

population = []
for day in range(days):
    locations = {}
    for l in range(lnum):
        locations[l] = 0
    births = 0
    deaths = 0

    for dove in range(doves):
        location = random.randint(0, lnum-1)
        if locations[location] < 2:
            locations[location] += 1
        else:
            deaths += 1
            print(f'death at {location}')

    for location in locations:
        if locations[location] == 1:
            print(f'birth at {location}')
            births += 1

    doves -= deaths
    doves += births

    population.append(doves)
    print(f'Day {day} Summary:\nPopulation: {doves} Deaths:{deaths} Births: {births}\n')

plt.plot(population)
plt.xlabel('Days')
plt.ylabel('Population')
plt.show()
