import random
import matplotlib.pyplot as plt

# Initial populations of doves and hawks
doves = 10
hawks = 0

# Total number of days the simulation will run for
days = 50
# Number of available locations with food
lnum = 100

population = []

# Each day...
for day in range(days):
    # A dict to store the number of creatures occupying a location at any day
    locations = {}
    # Intialize each location with zero creatures
    for l in range(lnum):
        locations[l] = 0

    births = 0
    deaths = 0

    # For each creature, randomize its location
    for dove in range(doves):
        location = random.randint(0, lnum-1)
        # If vacant, occupy :)
        if locations[location] < 2:
            locations[location] += 1
        # Else, no food, die :(
        else:
            deaths += 1
            print(f'death at {location}')

    # If location only occupied by one creature, can reproduce
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
