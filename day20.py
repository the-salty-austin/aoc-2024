from collections import defaultdict
import heapq

def parse_input(filename):
    grid = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            grid.append([char for char in line])

    return grid


def solve1(grid, minsave):
    si, sj, ei, ej = 0,0,0,0
    N, M = len(grid), len(grid[0])
    def inside(i,j):
        return 0<=i<N and 0<=j<M

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                si, sj = i, j
            elif grid[i][j] == 'E':
                ei, ej = i, j
    
    h = [(0, si, sj, 0, 0)]
    path = []
    cost = {}
    while h:
        c, i, j, pi, pj = h.pop()
        if grid[i][j] == "#":
            continue
        else:
            path.append((i,j))
            cost[(i,j)] = c
        if grid[i][j] == "E": break
        
        nxt = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        for ni, nj in nxt:
            if (ni,nj) == (pi,pj): continue
            h.append((c+1, ni,nj,i,j))


    savings = {}
    count = 0
    for i,j in path:
        nxt = [(i+2,j),(i-2,j),(i,j+2),(i,j-2)]
        thru = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        for x in range(len(nxt)):
            ni,nj = nxt[x]
            ti,tj = thru[x]
            if not inside(ni,nj) or grid[ni][nj] == '#':
                continue
            if cost[(ni,nj)] - cost[(i,j)] - 2 >= minsave and grid[ti][tj] == '#':
                savings[(i,j,ni,nj)] = cost[(ni,nj)] - cost[(i,j)] - 2
                count += 1
    
    print(f"Part One - {count}") # 1518



def solve2(grid, minsave):
    si, sj, ei, ej = 0,0,0,0
    N, M = len(grid), len(grid[0])
    def inside(i,j):
        return 0<=i<N and 0<=j<M

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                si, sj = i, j
            elif grid[i][j] == 'E':
                ei, ej = i, j
    
    h = [(0, si, sj, 0, 0)]
    path = []
    cost = {}
    while h:
        c, i, j, pi, pj = h.pop()
        if grid[i][j] == "#":
            continue
        else:
            path.append((i,j))
            cost[(i,j)] = c
        if grid[i][j] == "E": break
        
        nxt = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        for ni, nj in nxt:
            if (ni,nj) == (pi,pj): continue
            h.append((c+1, ni,nj,i,j))

    savings = {}
    count = 0
    for i,j in path:
        for step in range(2, 21): # step as manhatten distance
            for di in range(step+1):
                dj = step - di
                nxt = [(i+di,j+dj),(i+di,j-dj),(i-di,j+dj),(i-di,j-dj)]
                for x in range(len(nxt)):
                    ni,nj = nxt[x]
                    if not inside(ni,nj) or grid[ni][nj] == '#' or (i,j,ni,nj) in savings:
                        continue
                    if cost[(ni,nj)] - cost[(i,j)] - step >= minsave:
                        savings[(i,j,ni,nj)] = cost[(ni,nj)] - cost[(i,j)] - step
                        count += 1
    
    print(f"Part Two - {count}") # 1032257


# grid = parse_input('./inputs/day20toy.txt')
# solve1(grid, 0)
# solve2(grid, 50)

grid = parse_input('./inputs/day20.txt')
solve1(grid, 100)
solve2(grid, 100)