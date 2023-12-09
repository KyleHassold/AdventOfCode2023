### Imports ###

from time import time

### Methods ###

def extrapolate(data: list[int]):
    # Get differences
    diffs = [data[i+1]-data[i] for i in range(len(data)-1)]
    
    # Check if any values are non-zero
    if any(diffs):
        back, forward = extrapolate(diffs)
        return diffs[0] - back, diffs[-1] + forward
    return 0, 0


### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 9: Mirage Maintenance...\n")
    start = time()

    part1_sol = 0
    part2_sol = 0

    lines = []
    with open('./day9/input.txt', 'r') as f:
        for l in f:
            data = [int(n) for n in l.split()]
            back, forward = extrapolate(data)

            part1_sol += data[-1] + forward
            part2_sol += data[0] - back

    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)