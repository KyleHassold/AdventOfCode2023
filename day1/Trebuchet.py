### Imports ###

from time import time
import re


### Methods ###

def clean_str(s: str, include_alpha = False):
    nums = ['one', "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    reg = '^([0-9]'
    if include_alpha:
        reg += '|' + '|'.join(nums)
    reg += ')'

    new_s = ''
    while s:
        groups = re.search(reg, s)
        s = s[1:]
        if groups is None:
            pass
        elif groups.groups()[0].isdigit():
            new_s += groups.groups()[0]
        else:
            new_s += str(nums.index(groups.groups()[0])+1)
    return new_s


### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 1: Trebuchet?!...\n")
    start = time()

    part1_sol = 0
    part2_sol = 0

    with open('./day1/input.txt', 'r') as f:
        for l in f:
            cleaned = clean_str(l)
            part1_sol += int(cleaned[0] + cleaned[-1])
            cleaned = clean_str(l, True)
            part2_sol += int(cleaned[0] + cleaned[-1])

    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)

