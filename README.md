* TOC {:toc}
# natural-selection
A collection of code inspired by [this series of youtube videos](https://www.youtube.com/watch?v=oDvzbBRiNlA&list=PLKortajF2dPBWMIS6KF4RLtQiG6KQrTdB) by [Primer.](https://www.youtube.com/channel/UCKzJFdi57J53Vr_BkTfN3uQ)

I've organized it by each concept examined that I found interesting.

## aggression
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


I first simulated a dove-only ecosystem, which started with 20 doves, had 100 unique locations, and ran for 100 days. The plot below shows how population varied with each day.
![](resources/plot.png)

The population shoots up immediately as there is a lower chance that creatures are overallocated to a single location. The code prints births, deaths, and a daily summary to the console. On Day 1, this is what it looks like:

![](resources/day1.png)

As quickly as Day 5, the deaths outnumber the births. This is because the population is greater than the number of locations, so fewer doves get to reproduce. This is shown in the console below.

![](resources/day5.png)
