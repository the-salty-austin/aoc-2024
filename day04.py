def find_xmas_occurrences(grid):
    n_row = len(grid)
    n_col = len(grid[0])
    target = "XMAS"
    total_occurrences = 0
    
    directions = [
        (0, 1),    # right
        (0, -1),   # left
        (1, 0),    # down
        (-1, 0),   # up
        (1, 1),    # down-right
        (-1, -1),  # up-left
        (1, -1),   # down-left
        (-1, 1)    # up-right
    ]
    
    def within_bounds(r, c):
        return 0 <= r < n_row and 0 <= c < n_col
    
    def check_word(r, c, dr, dc):
        if not within_bounds(r + dr*3, c + dc*3):
            return False

        for i in range(4):
            if grid[r + i*dr][c + i*dc] != target[i]:
                return False
        
        return True
    
    for r in range(n_row):
        for c in range(n_col):
            # all 8 directions
            for dr, dc in directions:
                if check_word(r, c, dr, dc):
                    total_occurrences += 1
    
    return total_occurrences

# inp = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX"
# ]

# inp = [
#     ".M.S......",
#     "..A..MSMS.",
#     ".M.S.MAA..",
#     "..A.ASMSM.",
#     ".M.S.M....",
#     "..........",
#     "S.S.S.S.S.",
#     ".A.A.A.A..",
#     "M.M.M.M.M.",
#     ".........."
# ]

def find_xmas_occurrences2(grid):
    n_row = len(grid)
    n_col = len(grid[0])
    target = "XMAS"
    total_occurrences = 0
    
    directions = [
        ( 1, 1),    # left-up to right-dn
        (-1, 1)  # left-dn to right-up
    ]
    
    def within_bounds(r, c):
        return 0 <= r < n_row and 0 <= c < n_col
    
    def check_word(r, c, dr, dc):
        if not within_bounds(r + dr, c + dc):
            return False
        if not within_bounds(r - dr, c - dc):
            return False

        if grid[r + dr][c + dc] == 'M':
            if grid[r - dr][c - dc] != 'S':
                return False
        elif grid[r + dr][c + dc] == 'S':
            if grid[r - dr][c - dc] != 'M':
                return False
        else:
            return False
        
        return True
    
    for r in range(n_row):
        for c in range(n_col):
            if grid[r][c] != 'A':
                continue

            if check_word(r, c, 1, 1) and check_word(r, c, -1, 1):
                total_occurrences += 1
    
    return total_occurrences

inp = list()
with open("./inputs/day04.txt") as f:
    for r in f:
        inp.append(r.strip())

print(find_xmas_occurrences(inp))

# ----------------------------- #
# ----------------------------- #
# ----------------------------- #

print(find_xmas_occurrences2(inp))