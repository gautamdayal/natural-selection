import random
import matplotlib.pyplot as plt

# Creature referred to as 'dove' because it is not competetive

# Initial populations of doves
doves = 10
hawks = 2

# Total number of days the simulation will run for
days = 1000
# Number of available locations with food
lnum = 100

dove_population = []
hawk_population = []

# Each day...
for day in range(days):
    print(f'\nDay {day}\n')
    # A dict to store the number of doves occupying a location at any day
    dove_locations = {}
    hawk_locations = {}
    # Intialize each location with zero doves
    for l in range(lnum):
        dove_locations[l] = 0
        hawk_locations[l] = 0

    dove_births = 0
    dove_deaths = 0
    hawk_births = 0
    hawk_deaths = 0

    # Repeat location selection process for hawks
    for hawk in range(hawks):
        location = random.randint(0, lnum-1)
        if dove_locations[location] + hawk_locations[location] < 2:
            hawk_locations[location] += 1
        else:
            hawk_deaths += 1
            print(f'- hawk at {location}')
    # For each dove, randomize its location
    for dove in range(doves):
        location = random.randint(0, lnum-1)
        # If vacant, occupy :)
        if dove_locations[location] + hawk_locations[location] < 2:
            dove_locations[location] += 1
        # Else, no food, die :(
        else:
            dove_deaths += 1
            print(f'- dove at {location}')

    for location in dove_locations:
        at_location = dove_locations[location] + hawk_locations[location]

        if dove_locations[location] == 1 and at_location == 1:
            print(f'+ dove at {location}')
            dove_births += 1
        elif hawk_locations[location] == 1 and at_location == 1:
            print(f'+ hawk at {location}')
            hawk_births += 1
        elif hawk_locations == 1 and at_location == 2:
            print(f'+ hawk at {location}')
            print(f'- dove at {location}')
            hawk_births += 1
            dove_deaths += 1
        elif hawk_locations[location] == 2:
            print(f'- hawk at {location}')
            hawk_deaths += 1


    # Adjust population accordingly
    doves += dove_births
    doves -= dove_deaths
    hawks += hawk_births
    hawks -= hawk_deaths

    dove_population.append(doves)
    hawk_population.append(hawks)


plt.plot(dove_population, label='doves')
plt.plot(hawk_population, label='hawks')
plt.xlabel('Days')
plt.ylabel('Population')
plt.legend()
plt.show()
