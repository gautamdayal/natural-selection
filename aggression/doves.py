import random
import matplotlib.pyplot as plt

# Creature referred to as 'dove' because it is not competetive

# Initial populations of doves
doves = 10

# Total number of days the simulation will run for
days = 50
# Number of available locations with food
lnum = 100

population = []

# Each day...
for day in range(days):
    # A dict to store the number of doves occupying a location at any day
    locations = {}
    # Intialize each location with zero doves
    for l in range(lnum):
        locations[l] = 0

    births = 0
    deaths = 0

    # For each dove, randomize its location
    for dove in range(doves):
        location = random.randint(0, lnum-1)
        # If vacant, occupy :)
        if locations[location] < 2:
            locations[location] += 1
        # Else, no food, die :(
        else:
            deaths += 1
            print(f'death at {location}')

    # If location only occupied by one dove, can reproduce
    for location in locations:
        if locations[location] == 1:
            print(f'birth at {location}')
            births += 1

    # Adjust population accordingly
    doves -= deaths
    doves += births

    population.append(doves)
    print(f'Day {day} Summary:\nPopulation: {doves} Deaths:{deaths} Births: {births}\n')

plt.plot(population)
plt.xlabel('Days')
plt.ylabel('Population')
plt.show()
