### Imports ###

from time import time


### Methods ###

def get_nums_loc(data: str):
    flag = False
    nums, symb, stars = [], [], []
    for i, c in enumerate(data):
        if c.isdigit():
            if flag:
                nums[-1][0] += c
            else:
                nums.append([c, i])
                flag = True
            continue

        flag = False
        if c != '.':
            symb.append(i)
            if c == '*':
                stars.append(i)
    
    return nums, symb, stars

def check_symbs(num, loc, symb_locs):
    for l in symb_locs:
        if loc - 1 <= l <= loc + len(num):
            return True
    return False

def check_stars(loc, nums, count = 2):
    prod = 1
    for n, num_loc in nums:
        if num_loc - 1 <= loc <= num_loc + len(n):
            count -= 1
            prod *= int(n)
    if count == 0:
        return prod
    return 0


### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 3: Gear Ratios...\n")
    start = time()

    part1_sol = 0
    part2_sol = 0

    lines = []
    with open('./day3/input.txt', 'r') as f:
        for l in f:
            lines.append(get_nums_loc(l[:-1]))

            if len(lines) > 3:
                lines.pop(0)
            elif len(lines) == 1:
                continue
            
            symbs = [sym for l in lines for sym in l[1]]
            for n, loc in lines[-2][0]:
                if check_symbs(n, loc, symbs):
                    part1_sol += int(n)

            nums = [n for l in lines for n in l[0]]
            for star in lines[-2][2]:
                part2_sol += check_stars(star, nums)
                    
        lines.pop(0)
        symbs = [sym for l in lines for sym in l[1]]
        for n, loc in lines[-2][0]:
            if check_symbs(n, loc, symbs):
                part1_sol += int(n)

        nums = [n for l in lines for n in l[0]]
        for star in lines[-2][2]:
            part2_sol += check_stars(star, nums)


    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)