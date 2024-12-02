data = list()

with open("./inputs/day02.txt") as f:
    for r in f:
        row = [int(x) for x in r.strip().split(' ')]
        data.append(row)

safe_cnt = 0
violation_dict = dict()
for di, row in enumerate(data):
    isIncreasing = True
    violation_pos = list()

    if row[0] > row[1]:
        isIncreasing = False

    for i in range(1, len(row)):
        if isIncreasing:
            if not ((row[i] > row[i-1]) and (1 <= abs(row[i] - row[i-1]) <= 3)):
                violation_pos.append(i)
        else:
            if not ((row[i] < row[i-1]) and (1 <= abs(row[i] - row[i-1]) <= 3)):
                violation_pos.append(i)
        
    violation_dict[di] = violation_pos

    safe_cnt += int(len(violation_pos)==0)

print("part one - Safe Count =", safe_cnt)

# # ---------------------------------------- # #

extra_cnt = 0
for di, row in enumerate(data):
    if len(violation_dict[di]) > 0:
        for skip in range(len(row)):
            sub_row = row[:skip] + row[skip+1:]
            is_increasing = all(sub_row[i] < sub_row[i + 1] for i in range(len(sub_row) - 1))
            is_decreasing = all(sub_row[i] > sub_row[i + 1] for i in range(len(sub_row) - 1))
            diffs = [abs(sub_row[i] - sub_row[i + 1]) for i in range(len(sub_row) - 1)]
            if (is_increasing or is_decreasing) and all(1 <= d <= 3 for d in diffs):
                extra_cnt += 1
                break

print("part two - Safe Count w 1-Removal =", safe_cnt + extra_cnt)
