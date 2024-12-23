# Source/Tutorial - https://www.youtube.com/watch?v=dqzAaj589cM

from collections import deque
from itertools import product
from functools import cache

NP = [
    ["7","8","9"],
    ["4","5","6"],
    ["1","2","3"],
    ['X','0',"A"]
] #numpad
AP = [
    ["X","^","A"],
    ["<","V",">"]
] #arrow pad

def parse_input(filename):
    inps = []
    numbers = []
    
    with open(filename, 'r') as file:
        for line in (file):
            line = line.strip()
            seenNonzero = False
            n = ""
            for x in line:
                if x != '0':
                    seenNonzero = True
                if seenNonzero or x != '0':
                    n += x
            numbers.append(int(n[:-1])) # remove A at the end
            inps.append(line)
    
    return inps, numbers

def precompute(keypad):
    pos = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[0])):
            if keypad[r][c] != 'X':
                pos[keypad[r][c]] = (r,c)
    seqs = {}
    for x in pos:
        for y in pos:
            if x==y:
                seqs[(x,y)] = ["A"]
                continue
            possibilities = []
            q = deque([(pos[x], "")]) # ((r,c), string_seq)
            optimal = float('inf')
            while q:
                (r,c), moves = q.popleft()
                for (nr, nc), nmove in [((r-1,c),"^"), ((r+1,c),"V"), ((r,c+1),">"), ((r,c-1),"<")]:
                    if not (0 <= nr < len(keypad)) or not (0 <= nc < len(keypad[0])): continue
                    if keypad[nr][nc] == 'X': continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves)+1: break
                        optimal = len(moves) + 1
                        possibilities.append(moves+nmove+"A")
                    else:
                        q.append(((nr,nc), moves+nmove))
                else:
                    continue # propagates "break" outwards
                break
            seqs[(x,y)] = possibilities
    
    return seqs

@cache
def compute_length(x,y, depth=2):
    if depth == 1:
        return arr_lens[(x,y)]
    optimal = float('inf')
    for moves in arr_seqs[(x,y)]: # reduce depth by one
        length = 0
        for x, y in zip("A"+moves, moves):
            length += compute_length(x,y, depth-1)
        optimal = min(optimal, length)
    return optimal

num_seqs = precompute(NP)
arr_seqs = precompute(AP)
arr_lens = {x2y_tuple: len(moves[0]) for x2y_tuple, moves in arr_seqs.items()}

def solve1(string, seqs):
# def solve1(string, keypad):
    # pos = {}
    # for r in range(len(keypad)):
    #     for c in range(len(keypad[0])):
    #         if keypad[r][c] != 'X':
    #             pos[keypad[r][c]] = (r,c)
    # seqs = {}
    # for x in pos:
    #     for y in pos:
    #         if x==y:
    #             seqs[(x,y)] = ["A"]
    #             continue
    #         possibilities = []
    #         q = deque([(pos[x], "")]) # ((r,c), string_seq)
    #         optimal = float('inf')
    #         while q:
    #             (r,c), moves = q.popleft()
    #             for (nr, nc), nmove in [((r-1,c),"^"), ((r+1,c),"V"), ((r,c+1),">"), ((r,c-1),"<")]:
    #                 if not (0 <= nr < len(keypad)) or not (0 <= nc < len(keypad[0])): continue
    #                 if keypad[nr][nc] == 'X': continue
    #                 if keypad[nr][nc] == y:
    #                     if optimal < len(moves)+1: break
    #                     optimal = len(moves) + 1
    #                     possibilities.append(moves+nmove+"A")
    #                 else:
    #                     q.append(((nr,nc), moves+nmove))
    #             else:
    #                 continue # propagates "break" outwards
    #             break
    #         seqs[(x,y)] = possibilities
    
    options = [seqs[(x,y)] for x,y in zip("A"+string, string)]
    return ["".join(x) for x in product(*options)]

# inps, numbers = parse_input('./inputs/day21toy.txt')
inps, numbers = parse_input('./inputs/day21.txt')

# ans1 = 0
# for inp, num in zip(inps, numbers):
#     print(num, inp)
#     # lvl_radioactives = solve1(inp, NP)
#     lvl_radioactives = solve1(inp, num_seqs)
#     lvl_colds = []
#     for lvlr in lvl_radioactives:
#         # lvl_colds.extend(solve1(lvlr, AP))
#         lvl_colds.extend(solve1(lvlr, arr_seqs))
#     minlen = min(map(len, lvl_colds))
#     lvl_colds = [seq for seq  in lvl_colds if len(seq)==minlen]
#     # print(lvl_colds)
#     lvl_manual = []
#     for lvlc in lvl_colds:
#         # lvl_manual.extend(solve1(lvlc, AP))
#         lvl_manual.extend(solve1(lvlc, arr_seqs))
#     minlen = min(map(len, lvl_manual))
#     lvl_manual = [seq for seq in lvl_colds if len(seq)==minlen]
#     print(minlen, num)
#     ans1 += minlen * num

# print(f"Part One - {ans1}")

##################
# ============== #
##################

ans2 = 0
for inp, num in zip(inps, numbers):
    lvl0 = solve1(inp, num_seqs)
    optimal = float("inf")
    for moves in lvl0:
        length = 0
        for x,y in zip("A"+moves, moves):
            length += compute_length(x,y, depth=25)
        optimal = min(optimal, length)
    print(optimal)
    ans2 += optimal * num

print(f"Part Two - {ans2}")