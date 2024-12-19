import re

def parse_input(filename):
    reg_txt = ['A', 'B', 'C']
    registers = {}
    program = []

    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip().split(' ')
            if i < 3:
                registers[reg_txt[i]] = int(line[-1])
            elif i == 4:
                program.extend([int(x) for x in line[-1].split(',')])
  
    return {"reg": registers, "prog": program}

class Processor:
    def __init__(self, reg, prog):
        self.A = reg['A']
        self.B = reg['B']
        self.C = reg['C']
        self.prog = prog

        self.opcode_pos = 0
        self.output = list()

    def run(self):
        while self.execute():
            pass
    
    def execute(self):
        if self.opcode_pos >= len(self.prog):
            return False # break the infinite loop in run()
        
        opcode = self.prog[self.opcode_pos]
        operand = self.prog[self.opcode_pos + 1]
        decoded_operand = self.decode_operand(operand)

        if opcode == 0:
            self.A = self.A // (2**decoded_operand)
        elif opcode == 1:
            self.B ^= operand # bitwise XOR
        elif opcode == 2:
            self.B = decoded_operand % 8
        elif opcode == 3:
            if self.A:
                self.opcode_pos = decoded_operand - 2 # -2 because +2 at the end
        elif opcode == 4:
            self.B ^= self.C
        elif opcode == 5:
            self.output.append(str(decoded_operand % 8))
        elif opcode == 6:
            self.B = self.A // (2**decoded_operand)
        elif opcode == 7:
            self.C = self.A // (2**decoded_operand)
        else:
            raise ValueError('Invalid Opcode')
        
        self.opcode_pos += 2
        return True

    def decode_operand(self, operand):
        if operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        elif operand == 6:
            return self.C
        elif operand == 7:
            raise ValueError('7 cannot be an operand')
        else:
            return operand
    
def solve1(inp):
    reg = inp['reg']
    prog = inp['prog']
    processor = Processor(reg, prog)
    processor.run()
    return ",".join(processor.output)

# source: https://www.youtube.com/watch?v=y-UPxMAh2N8
def solve2(prog):  
    def recursion(target, ans):
        if len(target) == 0: return ans
        for i in range(8):
            a = (ans << 3) | i # plus i
            b = 0
            c = 0
            out = None
            print(a, target)
            def decode_operand(operand):
                if 0 <= operand <= 3: return operand
                if operand == 4: return a
                if operand == 5: return b
                if operand == 6: return c
                if operand == 7: raise ValueError('7 cannot be an operand')

            for opcode_pos in range(0, len(prog)-2, 2):
                opcode = prog[opcode_pos]
                operand = prog[opcode_pos + 1]
                decoded_operand = decode_operand(operand)

                if opcode == 0:
                    # a = a >> decoded_operand
                    pass
                elif opcode == 1:
                    b = b ^ operand # bitwise XOR
                elif opcode == 2:
                    b = decoded_operand % 8
                elif opcode == 3:
                    raise AssertionError("program has JNZ inside expected loop body")
                elif opcode == 4:
                    b = b ^ c
                elif opcode == 5:
                    assert out is None, "program has multiple out"
                    out = decoded_operand % 8
                elif opcode == 6:
                    b = a >> decoded_operand
                elif opcode == 7:
                    c = a >> decoded_operand
                else:
                    raise ValueError('Invalid Opcode')
                if out == target[-1]:
                    sub = recursion(target[:-1], a)
                    if sub is None: continue
                    return sub

    return recursion(prog, 0)



inp = parse_input('./inputs/day17.txt')
# print(inp)
res = solve1(inp)
print(res) # 6,7,5,2,1,3,5,1,7

res = solve2(inp['prog'])
print(res)