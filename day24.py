def parse_input(filename):
    knowns = {}
    formulas = {}
    
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if line.isspace(): break
            x, y = line.split(': ')
            knowns[x] = int(y)

        for i, line in enumerate(file):
            x, op, y, z = line.replace("-> ", "").split()
            formulas[z] = (op, x, y)

    return knowns, formulas

OPERATORS = {
    "OR": lambda x, y: x | y,
    "AND": lambda x, y: x & y,
    "XOR": lambda x, y: x ^ y
}

def calc1(wire):
    if wire in knowns: return knowns[wire]
    op, x, y = formulas[wire]
    knowns[wire] = OPERATORS[op](calc1(x), calc1(y))
    return knowns[wire]

def solve1():
    z = []
    i = 0
    while True:
        key = "z" + str(i).rjust(2, "0") # make sure up the two digits, fill by 0.
        if key not in formulas: break # no more z's
        z.append(calc1(key))
        i += 1

    # print(z)
    # print("".join(map(str, z[::-1])))
    # print(int("".join(map(str, z[::-1])), 2))
    
def make_wire(char, num):
    return char + str(num).rjust(2, "0")

def verify_intermediate_xor(wire, num):
    # print("vx", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "XOR": return False
    return sorted([x,y]) == [make_wire("x", num), make_wire("y", num)]

def verify_direct_carry(wire, num):
    # print("vd", wire, num)
    if wire not in formulas: return False
    op,x,y = formulas[wire]
    if op != "AND": return False
    return sorted([x,y]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    # print("vr",wire,num)
    if wire not in formulas: return False
    op,x,y = formulas[wire]
    if op != "AND": return False
    return verify_intermediate_xor(x,num) and verify_carry_bit(y,num) or verify_intermediate_xor(y,num) and verify_carry_bit(x,num)

def verify_carry_bit(wire, num):
    # print("vc", wire, num)
    if wire not in formulas: return False
    op, x,y = formulas[wire]
    if num == 1:
        if op != 'AND': return False
        return sorted([x,y]) == ["x00", "y00"]
    if op != "OR": return False
    return verify_direct_carry(x,num-1) and verify_recarry(y,num-1) or verify_direct_carry(y, num-1) and verify_recarry(x, num-1)

def verify_z(wire, num):
    # print("vz", wire, num)
    if wire not in formulas: return False
    op, x, y = formulas[wire]
    if op != "XOR": return False
    if num == 0: return (sorted([x,y]) == ["x00", "y00"])
    return verify_intermediate_xor(x, num) and verify_carry_bit(y, num) or verify_intermediate_xor(y, num) and verify_carry_bit(x, num)

def verify(num):
    return verify_z(make_wire("z", num), num)

def progress():
    i = 0
    while True:
        if not verify(i): break
        i += 1

    return i



knowns, formulas = parse_input('./inputs/day24.txt')
solve1()

# PART TWO
swaps = []
for _ in range(4):
    baseline = progress()
    print(baseline)
    for x in formulas:
        for y in formulas:
            if x==y: continue
            formulas[x], formulas[y] = formulas[y], formulas[x]
            current = progress()
            if current > baseline:
                break
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break
    print(x, y)
    swaps += [x,y]
print("Part Two", ",".join(sorted(swaps)))