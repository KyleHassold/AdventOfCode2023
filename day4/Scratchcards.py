### Imports ###

from time import time

### Methods ###

def score(data: str):
    data = data.split(': ')[1]
    winning, available = [[int(n) for n in nums.split()] for nums in data.split(' | ')]
    count = len(set(winning).intersection(available))
    return count, int(pow(2, count-1))


### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 4: Scratchcards...\n")
    start = time()

    part1_sol = 0
    part2_sol = []

    lines = []
    with open('./day4/input.txt', 'r') as f:
        for i, l in enumerate(f):
            num, s = score(l[:-1])
            part1_sol += s
            while len(part2_sol) < i+num+1:
                part2_sol.append(1)
            for j in range(num):
                part2_sol[i+j+1] += part2_sol[i]

    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', sum(part2_sol[:i]))