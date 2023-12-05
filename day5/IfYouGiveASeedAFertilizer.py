### Imports ###

from time import time
import re

### Methods ###

map_flag = True
curr_source = ''
maps = {}

def make_maps(data: str):
    global map_flag, curr_source, maps

    # Start new mapping
    if map_flag:
        curr_source, dest = re.search(r'^([a-z]+)-to-([a-z]+) map:$', data).groups()
        maps[curr_source] = [dest, []]
        map_flag = False
    elif data != '\n':  # Add new mapping data
        dest, src, rang = re.search(r'^([0-9]+) ([0-9]+) ([0-9]+)$', data).groups()
        maps[curr_source][1].append({'src': int(src), 'dest': int(dest), 'range': int(rang)})
    else:  # Sort mapping data at the end of each mapping section
        maps[curr_source][1] = sorted(maps[curr_source][1], key=lambda x: x['src'])
        map_flag = True

def follow_maps(val, src):
    # Return final location value
    if src == 'location':
        return val
    dest = maps[src][0]

    # If below any existing maps
    if val < maps[src][1][0]['src']:
        return follow_maps(val, dest)

    # Find lowest mapping that starts higher than the value
    for i in range(1, len(maps[src][1])):
        if val < maps[src][1][i]['src']:
            # Check if value is within range of prior mapping
            if val < maps[src][1][i-1]['src'] + maps[src][1][i-1]['range']:
                return follow_maps(val - maps[src][1][i-1]['src'] + maps[src][1][i-1]['dest'], dest)
            # Between mappings
            return follow_maps(val, dest)
        
    else:
        # Check if value is in final mapping
        if val < maps[src][1][-1]['src'] + maps[src][1][-1]['range']:
            return follow_maps(val - maps[src][1][-1]['src'] + maps[src][1][-1]['dest'], dest)
        # Beyond final mapping
        return follow_maps(val, dest)

def follow_map_ranges(start, end, src):
    # Return final location value
    if src == 'location':
        return start
    
    dest = maps[src][0]
    mins = []

    # If range starts before any mappings
    if start < maps[src][1][0]['src']:
        mins.append(follow_map_ranges(start, min(end, maps[src][1][0]['src']), dest))
        # Move range start
        start = min(end, maps[src][1][0]['src'])

    # Continue checking ranges until input range is empty
    for i in range(1, len(maps[src][1])):
        if start >= end:
            return min(mins)
        
        # Find lowest mapping that starts higher than the input start
        if start < maps[src][1][i]['src']:
            # Check if input start is within range of prior mapping
            if start < maps[src][1][i-1]['src'] + maps[src][1][i-1]['range']:
                src_end = min(end - maps[src][1][i-1]['src'], maps[src][1][i-1]['range'])
                mins.append(follow_map_ranges(start - maps[src][1][i-1]['src'] + maps[src][1][i-1]['dest'],
                                              src_end + maps[src][1][i-1]['dest'], dest))
                # Move range start
                start = src_end + maps[src][1][i-1]['src']
            else:  # Start is beyond the range of the prior mapping
                min_end = min(end, maps[src][1][i]['src'])
                mins.append(follow_map_ranges(start, min_end, dest))
                start = min_end
    else:
        # Check if input range is empty
        if start >= end:
            return min(mins)
        # Check if start is within last range
        if start < maps[src][1][-1]['src'] + maps[src][1][-1]['range']:
            src_end = min(end - maps[src][1][-1]['src'], maps[src][1][-1]['range'])
            mins.append(follow_map_ranges(start - maps[src][1][-1]['src'] + maps[src][1][-1]['dest'],
                                            src_end + maps[src][1][-1]['dest'], dest))
            start = src_end + maps[src][1][-1]['src']
        # Remaining range is beyond mappings
        if start < end:
            mins.append(follow_map_ranges(start, end, dest))
    # Return minimum of all ranges
    return min(mins)


### Solve Puzzle ### 

if __name__ == '__main__':
    print("Solving Day 5: If You Give A Seed A Fertilizer...\n")
    start = time()

    part1_sol = 0
    part2_sol = 0

    lines = []
    with open('./day5/input.txt', 'r') as f:
        seeds = [int(s) for s in f.readline()[7:].split()]

        f.readline()
        for l in f:
            make_maps(l)

        # Sort last mapping
        maps[curr_source][1] = sorted(maps[curr_source][1], key=lambda x: x['src'])

        part1_sol = follow_maps(seeds[0], 'seed')
        for s in seeds[1:]:
            part1_sol = min(part1_sol, follow_maps(s, 'seed'))

        part2_sol = follow_map_ranges(seeds[0], seeds[0]+seeds[1], 'seed')
        for s in range(2, len(seeds), 2):
            part2_sol = min(part2_sol, follow_map_ranges(seeds[s], seeds[s]+seeds[s+1], 'seed'))


    print('Solved in {:.2f}ms'.format((time()-start)*1000))
    print('Part 1', part1_sol)
    print('Part 2', part2_sol)