# credit - https://github.com/mgtezak/Advent_of_Code/blob/master/2024/15/p2.py

from collections import defaultdict

def parse_input(filename):
    directionInput = False
    grid = []
    directions = []
    with open(filename, 'r') as file:
        for line in file:
            if line.isspace():
                directionInput = True
            line = line.strip()
            if directionInput:
                directions.extend(list(line))
            else:
                grid.append(list(line))

    return grid, directions

def solve1(grid, directions):
    N, M = len(grid), len(grid[0])
    for i in range(1, N-1):
        for j in range(1, M-1):
            if grid[i][j] == '@':
                ri, rj = i, j
                break


    for d in directions:
        # print("-"*20)
        # print('start', ri,rj, d)
        grid[ri][rj] = '.'
        if d == "<":
            jj = rj-1
            while grid[ri][jj] == 'O':
                jj -= 1
            if grid[ri][jj] == '.':
                # print(f"Swap {(ri,jj)} < {(ri, rj-1)}")
                grid[ri][jj], grid[ri][rj-1] = grid[ri][rj-1], grid[ri][jj]
                rj = rj-1
        elif d == "^":
            ii = ri - 1
            while grid[ii][rj] == 'O':
                ii -= 1
            if grid[ii][rj] == '.':
                # print(f"Swap {(ii,rj)} ^ {(ri-1, rj)}")
                grid[ii][rj], grid[ri-1][rj] = grid[ri-1][rj], grid[ii][rj]
                ri = ri-1
        elif d == ">":
            jj = rj+1
            while grid[ri][jj] == 'O':
                jj += 1
            if grid[ri][jj] == '.':
                # print(f"Swap {(ri,jj)} > {(ri, rj+1)}")
                grid[ri][jj], grid[ri][rj+1] = grid[ri][rj+1], grid[ri][jj]
                rj = rj+1
        elif d == "v":
            ii = ri + 1
            while grid[ii][rj] == 'O':
                ii += 1
            if grid[ii][rj] == '.':
                # print(f"Swap {(ii,rj)} v {(ri+1, rj)}")
                grid[ii][rj], grid[ri+1][rj] = grid[ri+1][rj], grid[ii][rj]
                ri = ri+1

        grid[ri][rj] = '@'
        # for row in grid:
        #     print(row)

    summ = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if grid[i][j] == "O":
                summ += 100*i + j
    return summ


def solve2(oldgrid, directions):
    N, M = len(oldgrid), len(oldgrid[0])
    grid = []
    for i in range(N):
        row = []
        for j in range(M):
            if oldgrid[i][j] == '@':
                row.extend(['@', '.'])
            elif oldgrid[i][j] == '.':
                row.extend(['.', '.'])
            elif oldgrid[i][j] == 'O':
                row.extend(['[', ']'])
            elif oldgrid[i][j] == '#':
                row.extend(['#', '#'])
        grid.append(row)

    # for row in grid:
    #     print(row)

    N, M = len(grid), len(grid[0])
    for i in range(1, N-1):
        for j in range(1, M-1):
            if grid[i][j] == '@':
                ri, rj = i, j
                break

    for d in directions:
        # print("-"*20)
        # print('start', ri,rj, d)
        grid[ri][rj] = '.'
        if d == "<":
            jj = rj-1
            while grid[ri][jj] == ']':
                jj -= 2
            if grid[ri][jj] == '.':
                # print(f"Swap {(ri,jj)} < {(ri, rj-1)}")
                for jjj in range(jj, rj):
                    grid[ri][jjj] = grid[ri][jjj+1]
                rj = rj-1
        elif d == ">":
            jj = rj+1
            while grid[ri][jj] == '[':
                jj += 2
            if grid[ri][jj] == '.':
                # print(f"Swap {(ri,jj)} > {(ri, rj+1)}")
                for jjj in range(jj, rj+1, -1):
                    grid[ri][jjj] = grid[ri][jjj-1]
                rj = rj+1
        elif d == "^":
            q = [(ri-1,rj)]
            canMove = True
            moveto = defaultdict(set)
            while q:
                x, y = q.pop()
                if grid[x][y] == '#':
                    canMove = False
                    break
                elif grid[x][y] == '[':
                    moveto[x].update({y,y+1})
                    q.extend([(x-1,y), (x-1,y+1)])
                elif grid[x][y] == ']':
                    moveto[x].update({y-1,y})
                    q.extend([(x-1,y-1), (x-1,y)])
                elif grid[x][y] == '.':
                    moveto[x].update({y})
            
            if canMove:
                for x in sorted(moveto):
                    for y in moveto[x]:
                        grid[x][y] = grid[x+1][y] if y in moveto[x+1] else '.'
                ri -= 1
        
        elif d == "v":
            q = [(ri+1,rj)]
            canMove = True
            moveto = defaultdict(set)
            while q:
                x, y = q.pop()
                # print(x,y)
                if grid[x][y] == '#':
                    canMove = False
                    # print('break')
                    break
                elif grid[x][y] == '[':
                    moveto[x].update({y,y+1})
                    q.extend([(x+1,y), (x+1,y+1)])
                elif grid[x][y] == ']':
                    moveto[x].update({y-1,y})
                    q.extend([(x+1,y-1), (x+1,y)])
                elif grid[x][y] == '.':
                    moveto[x].update({y})
            
            if canMove:
                # print('moving donw')
                for x in sorted(moveto, reverse=True):
                    for y in moveto[x]:
                        grid[x][y] = grid[x-1][y] if y in moveto[x-1] else '.'
                
                ri += 1

        grid[ri][rj] = '@'
        # for row in grid:
        #     print(row)

    summ = 0
    for i in range(1,N-1):
        for j in range(2,M-2):
            if grid[i][j] == "[":
                summ += 100*i + j
    return summ

# # grid, directions = parse_input('./inputs/day15toy2.txt')
grid, directions = parse_input('./inputs/day15.txt') 
# ans1 = solve1(grid, directions)
# print(f"Part ONE - {ans1}")

grid, directions = parse_input('./inputs/day15.txt') 
ans2 = solve2(grid, directions)
print(f"Part TWO - {ans2}")
