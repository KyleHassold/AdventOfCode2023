### Imports ###

from time import time
import re
import math

### Methods ###

def get_margin(time: int, dist: int):
    upper_margin = (-time - (time**2 - 4*dist)**0.5) / -2
    lower_margin = time - upper_margin
    margin = int(upper_margin) - int(lower_margin)
    return margin + (-1 if upper_margin.is_integer() else 0)



### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 6: Wait For It...\n")
    start = time()

    part1_sol = 1
    part2_sol = 0

    with open('./day6/input.txt', 'r') as f:
        times = [int(s) for s in f.readline().split()[1:]]
        big_time = int(''.join([str(t) for t in times]))
        distances = [int(s) for s in f.readline().split()[1:]]
        big_dist = int(''.join([str(d) for d in distances]))
    
    for t, d in zip(times, distances):
        part1_sol *= get_margin(t, d)
    part2_sol = get_margin(big_time, big_dist)

    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)