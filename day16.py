import numpy as np
from collections import defaultdict
import heapq

def parse_input(filename):
    grid = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            grid.append([char for char in line])

    return grid

def solve1(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])

    si, sj = n_rows-2, 1

    def bfs(y,x):
        visited = set()
        q = [(0, y, x, y, x-1)]
        heapq.heapify(q)

        mincost = 1e10
        while q:
            curcost, cury, curx, prevy, prevx = heapq.heappop(q)
            dy, dx = cury-prevy, curx-prevx
            if grid[cury][curx] == '#': 
                continue
            if (cury, curx, dy, dx) in visited:
                continue
            if grid[cury][curx] == 'E':
                return curcost

            visited.add((cury,curx,dy,dx))
            
            nextsteps = [
                (curcost + 1, cury+dy, curx+dx, cury, curx),
                (curcost + 1001, cury+dx, curx-dy, cury, curx),
                (curcost + 1001, cury-dx, curx+dy, cury, curx)
            ]

            for step  in nextsteps:
                heapq.heappush(q, step)

        return float('inf')

    result = bfs(si, sj)
    return result

def solve2(grid):
    # credit - https://www.youtube.com/watch?v=ydrvSQuP1Aw
    n_rows = len(grid)
    n_cols = len(grid[0])

    si, sj = n_rows-2, 1

    cost = defaultdict(lambda: 10**20)
    prev = defaultdict(list)

    visited = set()
    gone = set()

    def bfs(y,x):
        q = [(0, y, x, 0, 1)]
        heapq.heapify(q)

        def go_backwards(y,x,dy,dx):
            if (y,x,dy,dx) in gone:
                return
            gone.add((y,x,dy,dx))
            visited.add((y,x))
            for py,px,pdy,pdx in prev[(y,x,dy,dx)]:
                go_backwards(py,px,pdy,pdx)

        while q:
            curcost, cury, curx, dy, dx = heapq.heappop(q)
            if cost[(cury,curx,dy,dx)] < curcost:
                continue

            if grid[cury][curx] == '#':
                continue

            if grid[cury][curx] == 'E':
                print(f'Part One - {curcost}')
                go_backwards(cury,curx,dy,dx)
                break

            if grid[cury+dy][curx+dx] != "#": # same dir, only 1 extra cost
                # print('same dir')
                if cost[(cury+dy,curx+dx,dy,dx)] > curcost + 1:
                    # print('push')
                    cost[(cury+dy,curx+dx,dy,dx)] = curcost + 1
                    prev[(cury+dy,curx+dx,dy,dx)] = [(cury,curx,dy,dx)] # reset the list for backtracking
                    heapq.heappush(q, (curcost+1, cury+dy,curx+dx,dy,dx))
                elif cost[(cury+dy,curx+dx,dy,dx)] == curcost + 1:
                    prev[(cury+dy,curx+dx,dy,dx)].append((cury,curx,dy,dx))

            # just turning, no movement (dy,dx) -> (dx,-dy)
            if cost[(cury,curx,dx,-dy)] > curcost + 1000:
                cost[(cury,curx,dx,-dy)] = curcost + 1000
                prev[(cury,curx,dx,-dy)] = [(cury,curx,dy,dx)]
                heapq.heappush(q, (curcost+1000, cury,curx,dx,-dy))
            elif cost[(cury,curx,dx,-dy)] == curcost + 1000:
                prev[(cury,curx,dx,-dy)].append((cury,curx,dy,dx))

            # just turning, no movement (dy,dx) -> (-dx,dy)
            if cost[(cury,curx,-dx,dy)] > curcost + 1000:
                cost[(cury,curx,-dx,dy)] = curcost + 1000
                prev[(cury,curx,-dx,dy)] = [(cury,curx,dy,dx)]
                heapq.heappush(q, (curcost+1000, cury, curx,-dx,dy))
            elif cost[(cury,curx,-dx,dy)] == curcost + 1000:
                # print('turn 2b')
                prev[(cury,curx,-dx,dy)].append((cury,curx,dy,dx))

    bfs(si, sj)
    return len(visited)

def solve2a(grid):
    """Solves both parts of the problem."""
    m = grid
    INF = 10**20
    dist = defaultdict(lambda: INF)
    prev = defaultdict(list)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    # Find start (S) and end (E) positions
    for r, row in enumerate(m):
        for c, val in enumerate(row):
            if val == "S":
                sx, sy = r, c
            elif val == "E":
                ex, ey = r, c

    h = []
    heapq.heappush(h, (0, sx, sy, 0))  # (distance, x, y, direction)
    dist[(sx, sy, 0)] = 0
    seen = set()

    def go(x, y, dr):
        """Recursively traces back the path to find all visited tiles."""
        if (x, y, dr) not in seen:
            seen.add((x, y, dr))
            for nx, ny, ndr in prev[(x, y, dr)]:
                go(nx, ny, ndr)

    while h:
        d, x, y, dr = heapq.heappop(h)
        if dist[(x, y, dr)] < d:
            continue

        if (x, y) == (ex, ey):
            print("Part 1:", d)  # Print the result for Part 1
            go(x, y, dr)  # Trace back the path for Part 2
            break

        dx, dy = directions[dr]
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(m) and 0 <= ny < len(m[0]) and m[nx][ny] != "#":
            nd = d + 1  # Cost for moving straight
            if dist[(nx, ny, dr)] > nd:
                dist[(nx, ny, dr)] = nd
                heapq.heappush(h, (nd, nx, ny, dr))
                prev[(nx, ny, dr)] = [(x, y, dr)]
            elif dist[(nx, ny, dr)] == nd:
                prev[(nx, ny, dr)].append((x, y, dr))

        for dd in [-1, 1]:  # Try turning left and right
            ndr = (dr + dd) % 4
            nd = d + 1000  # Cost for turning
            if dist[(x, y, ndr)] > nd:
                dist[(x, y, ndr)] = nd
                heapq.heappush(h, (nd, x, y, ndr))
                prev[(x, y, ndr)] = [(x, y, dr)]
            elif dist[(x, y, ndr)] == nd:
                prev[(x, y, ndr)].append((x, y, dr))

    print("Part 2:", len(seen))  # 684 too high

grid = parse_input('./inputs/day16.txt')
# print(grid)
# solve1(grid)
result = solve1(grid)
print(f"Part 1 - {result}")

result = solve2(grid)
print(f"Part 2 - {result}")