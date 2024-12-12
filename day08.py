from collections import defaultdict

def parse_input(fpath):
    grid = list()
    with open(fpath, 'r') as f:
        for r in f:
            grid.append([char for char in r.strip()])

    return grid

# Optimize by using direction and distance calculations
def check_antinodes(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    candidates = [
        (x1 - dx, y1 - dy),
        (x2 + dx, y2 + dy) 
    ]
    
    return [
        (x, y) for x, y in candidates 
        if 0 <= x < n_rows and 0 <= y < n_cols
    ]

def check_antinodes2(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    
    anti = [(x1,y1), (x2,y2)]
    x, y = x2, y2
    while (0 <= x+dx < n_rows and 0 <= y+dy < n_cols):
        x += dx
        y += dy
        anti.append((x,y))
    
    x, y = x1,y1
    while (0 <= x-dx < n_rows and 0 <= y-dy < n_cols):
        x -= dx
        y -= dy
        anti.append((x,y))
    
    return anti

def find_antinodes1(grid):
    antennas = defaultdict(list)
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] != '.':
                antennas[grid[r][c]].append((r, c)) # e.g. {A: [(2,5), (5,3), ...]}
    
    print(antennas)
    antinodes = set() # results stored here
    
    for freq, locations in antennas.items():
        # Only process frequencies with multiple antennas
        if len(locations) > 1:
            for i in range(len(locations)):
                for j in range(i+1, len(locations)):
                    x1, y1 = locations[i]
                    x2, y2 = locations[j]

                    anti = check_antinodes(x1, y1, x2, y2)
                    print(f"[{freq}] {x1},{y1}-{x2},{y2} > {anti}")
                    antinodes.update(anti)
    
    return antinodes

def find_antinodes2(grid):
    antennas = defaultdict(list)
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] != '.':
                antennas[grid[r][c]].append((r, c)) # e.g. {A: [(2,5), (5,3), ...]}
    
    print(antennas)
    antinodes = set() # results stored here
    
    for freq, locations in antennas.items():
        # Only process frequencies with multiple antennas
        if len(locations) > 1:
            for i in range(len(locations)):
                for j in range(i+1, len(locations)):
                    x1, y1 = locations[i]
                    x2, y2 = locations[j]

                    anti = check_antinodes2(x1, y1, x2, y2)
                    print(f"[{freq}] {x1},{y1}-{x2},{y2} > {anti}")
                    antinodes.update(anti)
    
    return antinodes


grid = parse_input('./inputs/day08.txt')
n_rows, n_cols = len(grid), len(grid[0])

result = find_antinodes1(grid)
# print(result)
print(f"Number of unique antinode locations: {len(result)}")

result = find_antinodes2(grid)
print(f"Number of unique antinode locations: {len(result)}")