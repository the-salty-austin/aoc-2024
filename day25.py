def parse_input(filename):
    locks = []
    keys = []
    block = []

    i = 0
    isLock = False
    with open(filename, 'r') as file:
        for line in (file):
            if line.isspace():
                height = []
                if block[0][0] == '#': # lock
                    for j in range(len(block[0])):
                        for i in range(1,len(block)):
                            if block[i][j] != '#':
                                height.append(i-1)
                                break
                    locks.append(height)
                else:
                    for j in range(len(block[0])):
                        for i in range(len(block)-2,-1,-1):
                            if block[i][j] != '#':
                                height.append(5-i)
                                break
                    keys.append(height)

                block = []
                continue
            line = [*line.strip()]
            block.append(line)
        
        height = [] # last block (nothing beneath)
        if block[0][0] == '#': # lock
            for j in range(len(block[0])):
                for i in range(1,len(block)):
                    if block[i][j] != '#':
                        height.append(i-1)
                        break
            locks.append(height)
        else:
            for j in range(len(block[0])):
                for i in range(len(block)-2,-1,-1):
                    if block[i][j] != '#':
                        height.append(5-i)
                        break
            keys.append(height)

    return locks, keys


def solve1():
    ans = 0
    fit = True
    for lock in locks:
        for key in keys:
            for l,k in zip(lock,key):
                if (l+k) > 5:
                    fit = False
                    break
            if fit:
                print(lock, key)
                ans += 1
            fit = True

    return ans


# locks, keys = parse_input('./inputs/day25toy.txt')
locks, keys = parse_input('./inputs/day25.txt')
ans1 = solve1()
print(f"Part One - {ans1}")
