### Imports ###

from time import time
from functools import cmp_to_key

### Methods ###

def get_type(hand: str):
    global joker
    cards = set(hand)

    # Five of a kind
    if len(cards) == 1:
        return 7
    # Four of a kind or Full house
    if len(cards) == 2:
        # Joker makes it Five of a kind
        if joker and 'J' in cards:
            return 7
        # Four of a kind
        if hand.count(next(iter(cards))) in [1, 4]:
            return 6
        # Full house
        return 5
    # Three of a kind or Two pair
    if len(cards) == 3:
        # Three of a kind
        if any([hand.count(c) == 3 for c in cards]):
            # Joker makes it Four of a kind
            if joker and 'J' in cards:
                return 6
            return 4
        # Two pair
        if joker and 'J' in cards:
            # 2 Jokers makes it Four of a kind
            if hand.count('J') == 2:
                return 6
            # 1 Joker makes it Full house
            return 5
        return 3
    # Pair
    if len(cards) == 4:
        # Joker makes it Three of a kind
        if joker and 'J' in cards:
            return 4
        return 2
    # High card, Joker makes it Pair
    if joker and 'J' in cards:
        return 2
    return 1

def compare_cards(a, b):
    global joker
    hier = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    # Change hierarchy for joker
    if joker:
        hier.append(hier.pop(3))

    for a_c, b_c in zip(a, b):
        if hier.index(a_c) < hier.index(b_c):
            return 1
        if hier.index(a_c) > hier.index(b_c):
            return -1
    return 0

def compare_type(a, b):
    if not a[2]:
        a[2] = get_type(a[0])
    if not b[2]:
        b[2] = get_type(b[0])

    if a[2] > b[2]:
        return 1
    if a[2] < b[2]:
        return -1
    return compare_cards(a[0], b[0])


### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 7: Camel Cards...\n")
    start = time()

    part1_sol = 0
    part2_sol = 0

    hands = []
    with open('./day7/input.txt', 'r') as f:
        for l in f:
            hands.append(l.split() + [0])
            hands[-1][1] = int(hands[-1][1])
    
    # Part 1
    joker = False
    hands.sort(key=cmp_to_key(compare_type))
    for i, (_, bid, _) in enumerate(hands):
        part1_sol += bid * (i + 1)

    # Reset store hand type
    for h in hands:
        h[2] = 0
    
    # Part 2
    joker = True
    hands.sort(key=cmp_to_key(compare_type))
    for i, (_, bid, _) in enumerate(hands):
        part2_sol += bid * (i + 1)

    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)