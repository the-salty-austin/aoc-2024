def parse_input(filename):
    grid = []
    starts = []
    
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip()
            grid.append([int(x) for x in line])
            for j, x in enumerate(line):
                if grid[i][j] == 0:
                    starts.append((i,j))
            

    return grid, starts


def solve1(grid, starts):
    N = len(grid)
    M = len(grid[0])
    def inside(i,j):
        return 0 <= i < N and 0 <= j < M
    
    totalsum = 0
    for k in range(len(starts)):
        si, sj = starts[k]
        visited = set()
        score = 0
        q = [(si,sj,-1)]
        while q:
            i,j,ph = q.pop()
            if not inside(i,j) or grid[i][j] - ph != 1:
                continue
            if grid[i][j] == 9 and (i,j) not in visited:
                # print(f'start from {(si,sj)}, found {(i,j)}')
                visited.add((i,j))
                score += 1
                continue
            for (di,dj) in [(-1,0), (1,0), (0,1), (0,-1)]:
                q.append((i+di, j+dj, grid[i][j]))
        # print(f"start from {(si,sj)} | Score {score}")
        totalsum += score

    print(f"Part One - {totalsum}")


def solve2(grid, starts):
    N = len(grid)
    M = len(grid[0])
    def inside(i,j):
        return 0 <= i < N and 0 <= j < M
    
    totalrating = 0
    for k in range(len(starts)):
        si, sj = starts[k]
        rating = 0
        q = [(si,sj,-1)]
        while q:
            i,j,ph = q.pop()
            if not inside(i,j) or grid[i][j] - ph != 1:
                continue
            if grid[i][j] == 9:
                # print(f'start from {(si,sj)}, found {(i,j)}')
                rating += 1
                continue
            for (di,dj) in [(-1,0), (1,0), (0,1), (0,-1)]:
                q.append((i+di, j+dj, grid[i][j]))
        # print(f"start from {(si,sj)} | Rating {rating}")
        totalrating += rating

    print(f"Part Two - {totalrating}")



# grid, starts = parse_input('./inputs/day10toy.txt')
grid, starts = parse_input('./inputs/day10.txt')

solve1(grid, starts)
solve2(grid, starts)