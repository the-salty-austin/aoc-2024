from collections import defaultdict

def parse_input(filename):
    grid = []
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            grid.append([x for x in line])

    return grid


def solve1(grid):
    N = len(grid)
    M = len(grid[0])
    def bfs(i, j):
        visited = set()
        curplant = grid[i][j]
        fence = 0
        queue = [(i,j)]
        while queue:
            nxti, nxtj = queue.pop()
            if (nxti, nxtj) in visited:
                continue
            if not (0 <= nxti < N) or not (0 <= nxtj < M) or (grid[nxti][nxtj] != curplant):
                fence += 1
                continue
            visited.add((nxti, nxtj))
            for ii, jj in [(nxti+1, nxtj), (nxti-1, nxtj), (nxti, nxtj+1), (nxti, nxtj-1)]:
                queue.append((ii, jj))

        cost = len(visited)*fence
        return visited,  cost
    
    cost_result = defaultdict(lambda: 0)
    tried = set()
    for i in range(N):
        for j in range(M):
            if (i,j) in tried:
                continue
            curplant = grid[i][j]
            visited, cost = bfs(i, j)
            cost_result[curplant] += cost

            tried.update(visited)
    
    total_cost = 0
    for plant in cost_result:
        total_cost += cost_result[plant]
    
    return total_cost


def solve2(grid):
    N = len(grid)
    M = len(grid[0])
    
    def within_bounds(i, j):
        return (0 <= i < N) and (0 <= j < M)

    def bfs(i, j):
        visited = set()
        curplant = grid[i][j]
        queue = [(i,j)]
        while queue:
            nxti, nxtj = queue.pop()
            if (nxti, nxtj) in visited:
                continue
            if not within_bounds(nxti, nxtj) or (grid[nxti][nxtj] != curplant):
                continue
            visited.add((nxti, nxtj))
            for ii, jj in [(nxti+1, nxtj), (nxti-1, nxtj), (nxti, nxtj+1), (nxti, nxtj-1)]:
                queue.append((ii, jj))

        return visited

    # credit for is_corner()
    # https://github.com/mgtezak/Advent_of_Code/blob/master/2024/12/p2.py
    def is_corner(i, j):
        thisplant = grid[i][j]
        # 8 directions (true means there's something in that direction)
        lu = (thisplant == grid[i-1][j-1]) if within_bounds(i-1, j-1) else False # left-up
        ll = (thisplant == grid[i  ][j-1]) if within_bounds(i  , j-1) else False # left
        ld = (thisplant == grid[i+1][j-1]) if within_bounds(i+1, j-1) else False # left-dn
        ru = (thisplant == grid[i-1][j+1]) if within_bounds(i-1, j+1) else False # right-up
        rr = (thisplant == grid[i  ][j+1]) if within_bounds(i  , j+1) else False # right
        rd = (thisplant == grid[i+1][j+1]) if within_bounds(i+1, j+1) else False # right-dn
        uu = (thisplant == grid[i-1][j  ]) if within_bounds(i-1, j  ) else False # up
        dd = (thisplant == grid[i+1][j  ]) if within_bounds(i+1, j  ) else False # dn

        is_corner = sum([
            # convex corners
            (not uu) and (not rr),
            (not uu) and (not ll), # -------+
            (not dd) and (not rr), # inside |
            (not dd) and (not ll),
            # concave corners
            uu and rr and (not ru),
            uu and ll and (not lu), # inside |
            dd and rr and (not rd), # inside +---
            dd and ll and (not ld)  #      inside
        ])

        return is_corner

    cost_result = defaultdict(lambda: 0)
    tried = set()
    for i in range(N):
        for j in range(M):
            if (i,j) in tried:
                continue
            curplant = grid[i][j]
            this_region = bfs(i, j)

            side_cnt = 0
            for (ri, rj) in this_region:
                side_cnt += is_corner(ri, rj)

            cost_result[curplant] += len(this_region) * side_cnt

            tried.update(this_region)
    
    total_cost = 0
    for plant in cost_result:
        total_cost += cost_result[plant]
    
    return total_cost


# grid = parse_input('./inputs/day12toy.txt')
grid = parse_input('./inputs/day12.txt')
ans = solve1(grid)
print('part one -',ans)

ans = solve2(grid)
print('part two -',ans)