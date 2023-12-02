### Imports ###

from functools import reduce
from time import time
import re


### Methods ###

def check_possible(revealed, max_vals):
    for s in revealed:
        for c in s:
            groups = re.search(r'^([0-9]+) (green|red|blue)$', c).groups()
            if int(groups[0]) > max_vals[groups[1]]:
                return False
    return True

def min_possible(revealed):
    min_vals = {'red': 0, 'green': 0, 'blue': 0}
    for s in revealed:
        for c in s:
            groups = re.search(r'^([0-9]+) (green|red|blue)$', c).groups()
            min_vals[groups[1]] = max(int(groups[0]), min_vals[groups[1]])
    return min_vals


### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 2: Cube Conundrum...\n")
    start = time()

    max_vals = {'red': 12, 'green': 13, 'blue': 14}
    part1_sol = 0
    part2_sol = 0

    with open('./day2/input.txt', 'r') as f:
        for line in f:
            id = re.search(r'^Game ([0-9]+):', line).groups()[0]
            line = line[7 + len(id):]
            revealed = [l.split(', ') for l in line.split('; ')]

            if check_possible(revealed, max_vals):
                part1_sol += int(id)

            counts = min_possible(revealed).values()
            part2_sol += reduce((lambda x, y: x * y), counts)
    
    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)