import re

# string = "mul(705,191) and mul(75,1) but not mul(5,1111)"
# pattern = r"mul\(\d{1,3},\d{1,3}\)"

# matches = re.findall(pattern, string)
# print(matches)

summ = 0
pattern = r"mul\(\d{1,3},\d{1,3}\)"

with open("./inputs/day03.txt") as f:
    for row in f:
        matches = re.findall(pattern, row)
        # print(matches)
        for match in matches:
            
            l = 4
            m = match.find(',')
            r = len(match)-1
            summ += int(match[l:m]) * int(match[m+1:r])


print('Part one - ', summ)

# ----------------- #

summ = 0
mult_pattern = r"mul\(\d{1,3},\d{1,3}\)"
disable_pattern = r"don\'t\(\)"
enable_pattern = r"do\(\)"

row = ""
with open("./inputs/day03.txt") as f:
    for r in f:
        row += r.strip()

mult_matches = list(re.finditer(mult_pattern, row))
disable_matches = list(re.finditer(disable_pattern, row))
enable_matches = list(re.finditer(enable_pattern, row))

all_matches = [(m, 'mul') for m in mult_matches] + [(m, 'dis') for m in disable_matches] + [(m, 'en') for m in enable_matches]

all_matches.sort(key=lambda x: x[0].start())

enabled = True

for m, typ in all_matches:
    if typ == 'mul' and enabled:
        txt = m.group(0)
        l, m, r = 4, txt.find(','), len(txt) - 1
        summ += int(txt[l:m]) * int(txt[m+1:r])
    elif typ == 'dis':
        enabled = False
    elif typ == 'en':
        enabled = True

print('Part two - ', summ)

# ----------------- #

# summ = 0
# row = ""
# with open("./inputs/day03.txt") as f:
#     for r in f:
#         row += r.strip()

# mult_matches = re.finditer(mult_pattern, row)
# d_pos = [match.start() for match in re.finditer(disable_pattern, row)]
# e_pos = [match.start() for match in re.finditer(enable_pattern, row)]

# di = 0
# ei = 0

# intervals = [[0, max(0, d_pos[0]-1)]]

# while (di < len(d_pos) or ei < len(e_pos)):
#     while (di < len(d_pos)):
#         if intervals[-1][1] != -1:
#             break
#         if d_pos[di] > intervals[-1][0] and intervals[-1][1] == -1:
#             intervals[-1][1] = d_pos[di] - 1
#             di += 1
#         else:
#             di += 1

#     while (ei < len(e_pos)):
#         if intervals[-1][1] == -1:
#             if (di >= len(d_pos)):
#                 ei = len(e_pos)
#             break
        
#         if e_pos[ei] > intervals[-1][1] and intervals[-1][1] != -1:
#             intervals.append( [e_pos[ei], -1] )
#             ei += 1
#             break
#         else:
#             ei += 1

# if intervals[-1][1] == -1:
#     intervals[-1][1] = len(row)-1

# inter_idx = 0
# for match in mult_matches:
#     start = match.start()
    
#     enabled = True
#     while (inter_idx < len(intervals)):
#         # print("cur interval:", intervals[inter_idx], "|", start)
#         if (inter_idx < len(intervals)-1) and (intervals[inter_idx][1] < start < intervals[inter_idx+1][0]):
#             enabled = False
#             break
#         elif (intervals[inter_idx][0] <= start <= intervals[inter_idx][1]):
#             enabled = True
#             break
#         else:
#             inter_idx += 1

#     if not enabled:
#         continue

#     txt = match.group(0)
#     l, m, r = 4, txt.find(','), len(txt) - 1
#     summ += int(txt[l:m]) * int(txt[m+1:r])


# print('Part two - ', summ)