list1 = list()
list2 = list()

with open("./inputs/day01.txt") as f:
    for row in f:
        tmp = row.strip().split('   ')
        list1.append(int(tmp[0]))
        list2.append(int(tmp[1]))

list1.sort()
list2.sort()

dist = 0
for i in range(len(list1)):
    dist += abs(list1[i] - list2[i])

print("Part One - Min Dist =", dist)

ptr1 = 0
ptr2 = 0
sim_score = 0

while(ptr1 < len(list1)):
    if list1[ptr1] < list2[ptr2]:
        ptr1 += 1
    elif list1[ptr1] > list2[ptr2]:
        ptr2 += 1
    else:
        cnt2 = 0
        while (list2[ptr2] == list1[ptr1]):
            cnt2 += 1
            ptr2 += 1
        cnt1 = 0
        while (list2[ptr2-1] == list1[ptr1]):
            cnt1 += 1
            ptr1 += 1
        sim_score += list1[ptr1-1] * cnt1 * cnt2

print("Part Two - Sim Score =", sim_score)