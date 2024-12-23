# Source: https://www.youtube.com/watch?v=kHIWvxRWQ9k

from collections import defaultdict

def parse_input(filename):
    connections = defaultdict(set)
    
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            x, y = line.strip().split('-')
            connections[x].add(y)
            connections[y].add(x)     

    return connections

def solve1(conns):
    sets = set()
    for x in conns:
        for y in conns[x]:
            if x==y: continue
            for z in conns[y]:
                if x != z and x in conns[z]:
                    sets.add(tuple(sorted([x,y,z])))
    
    return len([s for s in sets if any(cn.startswith("t") for cn in s)])

def solve2(conns):
    paths = set()
    def search(curnode, existing_set):
        path = tuple(sorted(existing_set))
        if path in paths: return
        paths.add(path)
        for neighbor in conns[curnode]:
            if neighbor in existing_set: continue
            if not all(neighbor in conns[query] for query in existing_set): continue
            # union operator "|" to add neighbor to existing_set
            search(neighbor, existing_set | {neighbor})
    
    for x in conns:
        search(x, {x})
    
    # print(paths)
    maxlen = max([len(s) for s in paths])
    for p in paths:
        if len(p) == maxlen:
            return ",".join(p)
    return "???"


# connections = parse_input('./inputs/day23toy.txt')
connections = parse_input('./inputs/day23.txt')
# print(connections)
ans1 = solve1(connections)
print(f"Part One - {ans1}")

ans2 = solve2(connections)
print(f"Part Two - {ans2}")