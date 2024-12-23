from collections import defaultdict

def parse_input(filename):
    lines = []
    
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip()
            lines.append(int(line))     

    return lines

def encrypt(num, steps=10):
    while steps:
        tmp = num * 64
        num ^= tmp
        num %= 16777216
        tmp = num // 32
        num ^= tmp
        num %= 16777216
        tmp = 2048 * num
        num ^= tmp
        num %= 16777216
        # print(num)
        steps -= 1
    
    return num

def difference(num, steps=10):
    diffs = []
    outs = []
    out = 0
    while steps:
        prevout = out
        out = num % 10
        # print(out)
        outs.append(out)
        diffs.append(out - prevout)
        tmp = num * 64
        num ^= tmp
        num %= 16777216
        tmp = num // 32
        num ^= tmp
        num %= 16777216
        tmp = 2048 * num
        num ^= tmp
        num %= 16777216  
        steps -= 1
    
    return diffs[1:], outs[4:]

def solve2(lines):
    gains = defaultdict(lambda: 0)
    maxprofit = 0
    best_seq = None
    for num in lines:
        diffs, outs = difference(num, steps=2000)
        seen = set()
        # print(outs, len(outs))
        # print(diffs, len(diffs))
        for end in range(3,len(diffs)):
            profit = outs[end-3]
            if tuple(diffs[end-3:end+1]) in seen: continue
            seen.add(tuple(diffs[end-3:end+1]))
            gains[tuple(diffs[end-3:end+1])] += profit
            if gains[tuple(diffs[end-3:end+1])] > maxprofit:
                maxprofit = gains[tuple(diffs[end-3:end+1])]
                best_seq = tuple(diffs[end-3:end+1])
    
    return maxprofit, best_seq

# lines = parse_input('./inputs/day22toy.txt')
lines = parse_input('./inputs/day22.txt')

ans1 = 0
for num in lines:
    encrypted = encrypt(num, steps=2000)
    ans1 += encrypted
    # print(f"[{num}] {encrypted}")
print(f"Part One - {ans1}")

maxprofit, best_seq = solve2(lines)
print(f"Part Two - {maxprofit}")
