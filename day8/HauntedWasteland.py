### Imports ###

from time import time
import re
import math

### Methods ###

def get_circle(node: str, instructions):
    z_history = {}
    step = 0
    while True:
        # Check if at an end point
        if node.endswith('Z'):
            # If end point have been visited
            if node in z_history:
                # If the endpoint has been visited at the same point in the instruction set
                for prev_step in z_history[node]:
                    if prev_step % len(instructions) == step % len(instructions):
                        # Return the initial visit and number of sets to circle
                        return prev_step, step - prev_step
                z_history[node].append(step)
            else:
                z_history[node] = [step]
        # Move forward
        inst = int(instructions[step%len(instructions)] == 'R')
        node = maps[node][inst]
        step += 1

### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 8: Haunted Wasteland...\n")
    start = time()

    part1_sol = 0
    part2_sol = 1

    maps = {}
    with open('./day8/input.txt', 'r') as f:
        instructions = f.readline()[:-1]
        f.readline()
        for i, l in enumerate(f):
            groups = re.search(r'^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)$', l).groups()
            maps[groups[0]] = (groups[1], groups[2])

    # Part 1
    node = 'AAA'
    while node != 'ZZZ':
        inst = int(instructions[part1_sol%len(instructions)] == 'R')
        node = maps[node][inst]
        part1_sol += 1

    # Part 2
    nodes = [k for k in maps.keys() if k.endswith('A')]
    # Offset is not needed for this
    dists = [get_circle(n, instructions)[1] for n in nodes]
    part2_sol = math.lcm(*dists)

    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)