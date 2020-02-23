#Here, we have a walk simulator that was originally made by a YouTuber named Socratica.

#This is my first Python program that uses Monte Carlo algorithms, it's also a good
#random example as well!

import random

def random_walk(n):
    """return coordinates after 'n' block random walk"""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)
#Our conventional testing method is down below:
#for i in range(25):
    #walk = random_walk(10)
    #print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

#No matter what amount of walks we take in the number_of_walks method, since Monte Carlo
#algorithms are based on random calculations within the range that we assign, the results
#will be different pretty much every time.
number_of_walks = int(input('How many walks are you taking? '))

for walk_length in range(1, 31):
    no_transport = 0 #Blocks 4 or fewer from home
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1

    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size = ", walk_length, 
    "/ % of no transport = ", 100*no_transport_percentage)

