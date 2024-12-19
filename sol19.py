from functools import cache
 
# D Y N A M I C  P R O G R A M M I N G
 
path = "./inputs/day19.txt"
# path = "test.txt"
 
with open(path) as f:
    input1, input2 = f.read().split('\n\n')
 
    patterns = frozenset([t.strip() for t in input1.split(',')])
    towels = [t.strip() for t in input2.splitlines()]
    
# print(patterns, towels)
 
@cache
def count_possibilities(patterns, towel: str):
    if len(towel) == 0:
        return 1
 
    count = 0
    for p in patterns:
        if towel.startswith(p):
            sub_towel = towel[len(p):]
            count += count_possibilities(patterns, sub_towel)
            
    
    return count
 
p1 = 0
p2 = 0
for t in towels:
    total = count_possibilities(patterns, t)
    if total > 0:
        p1 += 1
        print(t)
    # p1 += 1 if total > 0 else 0
    p2 += total
   
print('p1: ', p1)
print('p2: ', p2)