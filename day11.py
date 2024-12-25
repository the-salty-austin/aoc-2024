from collections import defaultdict

def parse_input(filename):
    numbers = []
    
    with open(filename, 'r') as file:
        for line in (file):
            numbers = line.strip().split()

    return numbers

def calc1(num):
    out = []
    s_num = str(num)
    l = len(s_num)
    if int(num) == 0:
        out = [1]
    elif l % 2 == 0: # even
        left, right = s_num[:l//2], s_num[l//2:]
        out = [int(left), int(right)]
        # print(int(left), int(right))
    else:
        out = [int(num) * 2024]
    # print(num, out)
    return out

def solve1(inps):
    blinks = 25
    while blinks:
        level = []
        for num in inps:
            out = calc1(num)
            level.extend(out)
        inps = [x for x in level]
        blinks -= 1
    
    return len(inps)

def solve2(inps):
    stones = {val: 1 for val in inps}
    blinks = 75
    while blinks:
        level_stones = defaultdict(lambda: 0)
        for stone, count in stones.items():
            for newstone in calc1(stone):
                level_stones[newstone] += count

        stones = level_stones
        blinks -= 1

    return sum(stones.values())


# inps = parse_input('./inputs/day11toy.txt')
inps = parse_input('./inputs/day11.txt')
print(inps)

ans1 = solve1(inps)
print(f"Part One - {ans1}")

ans2 = solve2(inps)
print(f"Part Two - {ans2}")
