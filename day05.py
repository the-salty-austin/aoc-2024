from collections import defaultdict

# ---------------------------- #
# --------- PART ONE --------- #
# ---------------------------- #

def extract_middle(update):
    return update[int(len(update) // 2)]

def is_valid1(rules_after, rules_before, update) -> bool:
    for cur in range(len(update)):
        for j in range(0, cur):
            if update[j] not in rules_before[update[cur]]:
                return False
        for j in range(cur+1, len(update)):
            if update[j] not in rules_after[update[cur]]:
                return False
        
    return True


# ---------------------------- #
# --------- PART TWO --------- #
# ---------------------------- #

# example update - 97,13,75,29,47
#
# rule:
# 97|75
# 29|13
# 47|13
#
# in-degree:
# 97: 0 in-degree
# 13: 2 in-degree (from 29 and 47)
# 75: 1 in-degree (from 97)
# 29: 0 in-degree
# 47: 0 in-degree
#
# start from lowest degree (pointed by fewest, should go first)
#
# example result - 29, 47, 97, 75, 13

def topological_sort(rules_before, rules_after, update: list) -> list:
    in_degree = {val: 0 for val in update}
    for val in update:
        for other in update:
            if other in rules_after[val]:
                in_degree[other] += 1

    result = []
    available = [p for p in update if in_degree[p] == 0]
    
    while available:W
        current = min(available)  # lexicographically smallest
        result.append(current)
        available.remove(current)
        
        for other in update:
            in_degree[other] -= 1
            if in_degree[other] == 0:
                available.append(other)
    
    return result

# ---------------------------- #
# --------- PART ONE --------- #
# ---------------------------- #

view_rules = True
rules_after = defaultdict(set)
rules_before = defaultdict(set)
updates = list()
with open("./inputs/day05.txt") as f:
    for r in f:
        if r.strip() == '':
            view_rules = False
        elif view_rules:
            a, b = r.strip().split('|')
            rules_after[a].add(b)
            rules_before[b].add(a)
        else:
            updates.append(r.strip().split(','))

sum1 = 0
incorrect_updates = list()
for update in updates:
    if is_valid1(rules_after, rules_before, update):
        sum1 += int(extract_middle(update))
    else:
        incorrect_updates.append(update)

print('part one -', sum1)

# ---------------------------- #
# --------- PART TWO --------- #
# ---------------------------- #

sum2 = 0
for update in incorrect_updates:
    res = topological_sort(rules_before, rules_after, update)
    sum2 += int(extract_middle(res))

print('part two -', sum2)