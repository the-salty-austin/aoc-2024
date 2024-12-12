def parse_input(fpath):
    targets = list()
    vals = list()
    with open(fpath, 'r') as f:
        for r in f:
            num, tmp = r.split(':')
            val = [int(x) for x in tmp.strip().split(' ')]
            
            targets.append(int(num))
            vals.append(val)

    return targets, vals

def solve1(target, val):
    def dfs(cur_index, accum):
        if cur_index < len(val)-1 and accum > target:
            return False
        if cur_index == len(val)-1:
            if accum == target:
                return True
            return False
        
        # return * or +
        return dfs(cur_index+1, accum * val[cur_index+1]) or dfs(cur_index+1, accum + val[cur_index+1])
    
    return dfs(0, val[0])

def solve2(target, val):
    def dfs(cur_index, accum):
        if cur_index < len(val)-1 and accum > target:
            return False
        if cur_index == len(val)-1:
            if accum == target:
                return True
            return False
        
        mult = dfs(cur_index+1, accum * val[cur_index+1]) if accum else False
        add  = dfs(cur_index+1, accum + val[cur_index+1])

        concat_val = accum * 10**len(str(val[cur_index+1])) + val[cur_index+1]
        concat = dfs(cur_index+1, concat_val)

        return mult or add or concat
    
    return dfs(-1, 0)

targets, vals = parse_input('./inputs/day07.txt')

summ = 0
for target, val in zip(targets, vals):
    if solve1(target, val):
        summ += target

print('part one -', summ)

summ = 0
for target, val in zip(targets, vals):
    if solve2(target, val):
        summ += target

print('part two -', summ)