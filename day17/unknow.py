### Imports ###

from time import time
import re

### Methods ###

def helper(data: str):
    pass


### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 17: ...\n")
    start = time()

    part1_sol = 0
    part2_sol = 0

    lines = []
    with open('./day17/input.txt', 'r') as f:
        for i, l in enumerate(f):
            pass

    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)