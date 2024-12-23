from collections import deque
# NP = [
#     ["7","8","9"],
#     ["4","5","6"],
#     ["1","2","3"],
#     ['X','0',"A"]
# ] #numpad
# AP = [
#     ["X","^","A"],
#     ["<","V",">"]
# ] #arrow pad
NP = {
    "7": (0,0), "8": (0,1), "9": (0,2),
    "4": (1,0), "5": (1,1), "6": (1,2),
    "1": (2,0), "2": (2,1), "3": (2,2),
                "0": (3,1), "A": (3,2)
}
AP = {
                   (-1,0): (0,1),  "A" : (0,2),
    (0,-1): (1,0), ( 1,0): (1,1), (0,1): (1,2)
}

def parse_input(filename):
    lines = []
    numbers = []
    
    with open(filename, 'r') as file:
        for line in (file):
            line = line.strip()
            tmp = [NP["A"]]
            seenNonzero = False
            n = ""
            for x in line:
                if x != '0':
                    seenNonzero = True
                if seenNonzero or x != '0':
                    n += x
                tmp.append(NP[x])
            numbers.append(int(n[:-1])) # remove A at the end
            lines.append(tmp)
    
    return lines, numbers

def sgn(x):
    if x>0: return 1
    elif x<0: return -1
    return 0

def solve1(inps, numbers):
    # this doesnt work because there are multiple ways to walk the manhatten distance.
    # e.g. want right 2 left 1. can do (>>^), (>^>), (^>>).
    ans = 0
    for inp, number in zip(inps, numbers):
        print(f"---- {inp} ----")
        all_manual = []
        lvl_radioactive = [AP["A"]]
        for k in range(1, len(inp)): # iterate on numpad
            dr = inp[k][0] - inp[k-1][0]
            dc = inp[k][1] - inp[k-1][1]
            # print(dc, dr)
            if (inp[k-1][0] == 3 and inp[k-1][1]+dc == 0):
                # goes outside
                if abs(dr): lvl_radioactive.extend([AP[(sgn(dr), 0)]] * abs(dr))
                if abs(dc): lvl_radioactive.extend([AP[(0, sgn(dc))]] * abs(dc))
            elif (inp[k-1][1] == 0 and inp[k-1][0]+dr == 3):
                # goes outside
                if abs(dc): lvl_radioactive.extend([AP[(0, sgn(dc))]] * abs(dc))
                if abs(dr): lvl_radioactive.extend([AP[(sgn(dr), 0)]] * abs(dr))
            else:
                if abs(dc): lvl_radioactive.extend([AP[(0, sgn(dc))]] * abs(dc))
                if abs(dr): lvl_radioactive.extend([AP[(sgn(dr), 0)]] * abs(dr))
            lvl_radioactive.append(AP["A"])
        print(f'radioactive k={k}', lvl_radioactive)
            
        lvl_cold = [AP["A"]]
        for kk in range(1, len(lvl_radioactive)):
            ddr = lvl_radioactive[kk][0] - lvl_radioactive[kk-1][0]
            ddc = lvl_radioactive[kk][1] - lvl_radioactive[kk-1][1]
            if (lvl_radioactive[kk-1][0] == 0 and lvl_radioactive[kk-1][1]+ddc == 0):
                # goes outside
                if abs(ddr): lvl_cold.extend([AP[(sgn(ddr), 0)]] * abs(ddr))
                if abs(ddc): lvl_cold.extend([AP[(0, sgn(ddc))]] * abs(ddc))
            elif (lvl_radioactive[kk-1][1] == 0 and lvl_radioactive[kk-1][0]+ddr == 0):
                # goes outside
                if abs(ddc): lvl_cold.extend([AP[(0, sgn(ddc))]] * abs(ddc))
                if abs(ddr): lvl_cold.extend([AP[(sgn(ddr), 0)]] * abs(ddr))
            else:
                if abs(ddc): lvl_cold.extend([AP[(0, sgn(ddc))]] * abs(ddc))
                if abs(ddr): lvl_cold.extend([AP[(sgn(ddr), 0)]] * abs(ddr))
            lvl_cold.append(AP["A"])
            # print("cold", lvl_cold)

        lvl_manual = [AP["A"]]
        for kkk in range(1, len(lvl_cold)):
            dddr = lvl_cold[kkk][0] - lvl_cold[kkk-1][0]
            dddc = lvl_cold[kkk][1] - lvl_cold[kkk-1][1]
            if (lvl_cold[kkk-1][0] == 0 and lvl_cold[kkk-1][1]+dddc == 0):
                # goes outside
                if abs(dddr): lvl_manual.extend([AP[(sgn(dddr), 0)]] * abs(dddr))
                if abs(dddc): lvl_manual.extend([AP[(0, sgn(dddc))]] * abs(dddc))
            elif (lvl_cold[kkk-1][1] == 0 and lvl_cold[kkk-1][0]+dddr == 0):
                # goes outside
                if abs(dddc): lvl_manual.extend([AP[(0, sgn(dddc))]] * abs(dddc))
                if abs(dddr): lvl_manual.extend([AP[(sgn(dddr), 0)]] * abs(dddr))
            else:
                if abs(dddc): lvl_manual.extend([AP[(0, sgn(dddc))]] * abs(dddc))
                if abs(dddr): lvl_manual.extend([AP[(sgn(dddr), 0)]] * abs(dddr))
            lvl_manual.append(AP["A"])
        all_manual.extend(lvl_manual)
        
        # print(all_manual)
        ans += (len(all_manual) - 1)  * number
        print(len(all_manual) - 1)
    print(f"Part One - {ans}") # 170508 too high


# inps, numbers = parse_input('./inputs/day21toy.txt')
inps, numbers = parse_input('./inputs/day21.txt')
solve1(inps, numbers)
# print(inps)
