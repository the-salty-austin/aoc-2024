import copy

DIRECTION = [
    (-1,0), # up
    (0, 1), # right
    ( 1,0), # down
    (0,-1)  # left
]

grid = list()
with open("./inputs/day06.txt") as f:
    for r in f:
        grid.append([char for char in r.strip()])

def get_start_position(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "^":
                return (r, c)

START_R, START_C = get_start_position(grid)

def is_inside(cur_r, cur_c):
    return (0 <= cur_r < len(grid)) and (0 <= cur_c < len(grid[0]))

def update_turn(r, c, turn_cnt: int, g: list) -> int:
    dr, dc = DIRECTION[turn_cnt % 4]
    if is_inside(r+dr, c+dc) and g[r+dr][c+dc] == '#':
        return True
    return False

def solve1(grid):
    covered = copy.deepcopy(grid) 
    turn_cnt = 0
    answer = 1

    r, c = START_R, START_C
    covered[r][c] = 'X'
    dr, dc = -1, 0 # default up
    while is_inside(r+dr, c+dc):
        turn_cnt += update_turn(r, c, turn_cnt, grid)
        dr, dc = DIRECTION[turn_cnt % 4]
        if (covered[r+dr][c+dc] != 'X'):
            answer += 1
        covered[r+dr][c+dc] = 'X'
        r += dr
        c += dc

    return answer, covered


def is_solution2(grid) -> bool:
    turn_cnt = 0
    r, c = START_R, START_C
    visited = set()
    dr, dc = -1, 0  # default up

    while is_inside(r + dr, c + dc):
        if (r + dr, c + dc, turn_cnt % 4) in visited:  
            return True

        visited.add((r + dr, c + dc, turn_cnt % 4))  

        while update_turn(r, c, turn_cnt, grid):
            """
            It's possible we need to make moere than one turn when we place obstacles.

            You are h. Going down intially.

            .h.       ...
            O..  -->  Oh. (You need to turn twice. To the left but hits O, so turn again)
            .#.       .#.
            """
            turn_cnt += 1
        
        dr, dc = DIRECTION[turn_cnt % 4]

        r += dr
        c += dc

    return False

def solve2(grid, covered1):
    answer = 0
    for pr in range(len(grid)):
        for pc in range(len(grid[0])):
            if grid[pr][pc] != '.': continue
            if covered1[pr][pc] != 'X': continue
            modified_grid = copy.deepcopy(grid)
            modified_grid[pr][pc] = '#'

            if is_solution2(modified_grid):
                answer += 1

    return answer

ans, covered1 = solve1(grid)
print('part one -', ans)

ans = solve2(grid, covered1)
print('part two -', ans)  # 15982 too high; 1889 too low