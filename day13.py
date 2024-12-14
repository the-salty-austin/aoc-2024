import re
import numpy as np

def parse_input(filename):
    machines = {}
    current_section = None
    
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            
            if not line: # skip empty lines
                continue

            if line.startswith('Button A:'):
                current_section = 'A'
                match = re.search(r'X\+(\d+), Y\+(\d+)', line)
                machines['A'] = list(map(int, (match.group(1), match.group(2))))
            
            elif line.startswith('Button B:'):
                current_section = 'B'
                match = re.search(r'X\+(\d+), Y\+(\d+)', line)
                machines['B'] = list(map(int, (match.group(1), match.group(2))))
            
            elif line.startswith('Prize:'):
                current_section = 'Prize'
                match = re.search(r'X=(\d+), Y=(\d+)', line)
                machines['Prize'] = list(map(int, (match.group(1), match.group(2))))

                if len(machines) == 3:
                    yield machines.copy()
                    machines.clear()

    if len(machines) == 3:
        yield machines

def solve1(machines):
    tokens = 0
    for machine in machines:
        mat = np.array([machine['A'], machine['B']])
        col = np.array(machine['Prize'])
        sol = np.linalg.solve(mat.T, col) 
        
        if np.all(np.isclose(sol, np.round(sol))):
            tokens += 3 * (sol[0]) + sol[1]
    
    return int(tokens)
 
def solve2(machines):
    tokens = 0
    for machine in machines:
        mat = np.array([machine['A'], machine['B']])
        col = np.array(machine['Prize']) + 10000000000000
        sol = np.linalg.solve(mat.T, col) 

        rounded_sol = np.array([round(x) for x in sol])
        all_integers = True
        for x, y in zip(sol, rounded_sol):
            if abs(x-y) > 1e-3:
                all_integers = False
                break
        if all_integers:
            tokens += 3 * (sol[0]) + sol[1]
    
    return int(tokens)

machines = list(parse_input('./inputs/day13.txt'))
res = solve1(machines)
print(res)

res = solve2(machines)
print(res)