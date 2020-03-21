A collection of code inspired by [this series of youtube videos](https://www.youtube.com/watch?v=oDvzbBRiNlA&list=PLKortajF2dPBWMIS6KF4RLtQiG6KQrTdB) by [Primer.](https://www.youtube.com/channel/UCKzJFdi57J53Vr_BkTfN3uQ)

I've organized it by each concept examined that I found interesting.

### table of contents
1. [aggression](#aggression)
    1. [doves only](#dovesonly)
    2. [doves and hawks](#dovesandhawks)

# aggression <a name="aggression"></a>
The first concept is the trait of aggression, and how it affects the population dynamic. In my code, I've simulated the classic game-theoretic _hawks and doves_ approach to the problem. Following is a short description of the algorithm. 
* Simulation runs for a specified number of days, and consists of a specified number of locations
* Each location has two pieces of food
* Each day, the location of each organism is randomized.
  * If an organism has a location to itself, it eats both pieces of food and can reproduce
  * If 2 doves meet, they each eat 1 piece and survive to the next day, but don't reproduce
  * If a dove and a hawk meet, the hawk takes more food, so it can reproduce, though the dove does not survive
  * If 2 hawks meet, this leads to a fight and they both do not survive
  * If an organism enters an occupied location, it does not survive

The table below summarizes the encounters and their consequences. 


|      | If dove            | If hawk           |
|------|------------------|----------------|
| meets dove | survive, survive | reproduce, die |
| meets hawk | die, reproduce   | die, die       |

## doves only <a name="dovesonly"></a>
I first simulated a dove-only ecosystem, which started with 20 doves, had 100 unique locations, and ran for 100 days. 

```python
# Initial populations of doves
doves = 10000

# Total number of days the simulation will run for
days = 200
# Number of available locations with food
lnum = 100
```
The location allocation process is simple, as shown below.

```python
for dove in range(doves):
        location = random.randint(0, lnum-1)
        # If vacant, occupy :)
        if locations[location] < 2:
            locations[location] += 1
        # Else, no food, die :(
        else:
            deaths += 1
            print(f'death at {location}')
```

The plot below shows how population varied with each day.
![](resources/plot.png)

The population shoots up immediately as there is a lower chance that creatures are overallocated to a single location. The code prints births, deaths, and a daily summary to the console. On Day 1, this is what it looks like:

![](resources/day1.png)

As quickly as Day 5, the deaths outnumber the births. This is because the population is greater than the number of locations, so fewer doves get to reproduce. This is shown in the console below.

![](resources/day5.png)

## doves and hawks <a name="dovesandhawks"></a>

For this section, I had a similar approach, though I needed a new set of variables and processes to take care of hawks: a tally of deaths and births, and I had to code up the consequence table shown earlier on this page. Here is the addition for assigning locations to hawks.

```python
# Repeat location selection process for hawks
    for hawk in range(hawks):
        location = random.randint(0, lnum-1)
        if dove_locations[location] + hawk_locations[location] < 2:
            hawk_locations[location] += 1
        else:
            hawk_deaths += 1
            print(f'- hawk at {location}')
```

Here is a simple implementation of the consequence table:

```python
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
            print(f'-- hawk at {location}')
            hawk_deaths += 2
```
One potential flaw is that in my current code, the location allocation process is ordered: one set of creatures is completely allocated before the other. Since being allocated to an occupied location could lead to decreases in population, this is unfair to the species located later in the order. Even after I allocated hawks _before_ doves, I get the following population graph. 

![](resources/plot2.png)
