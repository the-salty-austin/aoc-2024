from collections import defaultdict
import copy

def parse_input(fpath):
    info = list()
    blank = list()
    st = list()
    with open(fpath, 'r') as f:
        for r in f: #only one line
            current_file_id = 0
            for i, cnt in enumerate(r):
                cnt = int(cnt)
                if i % 2: # blank
                    blank.append(cnt)
                else: # info
                    info.append(cnt)
                    while cnt:
                        st.append(current_file_id)
                        cnt -= 1
                    current_file_id += 1

    return st, info, blank

def solve1(st, info_inp, blank_inp):
    info = copy.deepcopy(info_inp)
    blank = copy.deepcopy(blank_inp)
    filled_blanks = list()
    info_i = len(info) - 1
    info_cnt = sum(info)
    for i, empty_cnt in enumerate(blank):
        tmp = list()
        info_cnt -= info[i]
        while (empty_cnt and info_cnt):
            tmp.append(st.pop())
            if info[info_i] == 0: # cur id used up,
                info_i -= 1 # go to next (smaller) id
            info[info_i] -= 1 # remaining count for that id
            info_cnt -= 1
            empty_cnt -= 1
        filled_blanks.append(tmp)

    arr = list()
    for cur_val, cur_len in enumerate(info):
        while (cur_len):
            arr.append(cur_val)
            cur_len -= 1
        if cur_val < len(info)-1:
            arr.extend(filled_blanks[cur_val])
    
    checksum = 0
    for i, v in enumerate(arr):
        checksum += (i*v)
    return checksum


def solve2(info_inp, blank_inp):
    info = copy.deepcopy(info_inp)
    blank = copy.deepcopy(blank_inp)
    starting_blank = copy.deepcopy(blank_inp)
    starting_info = copy.deepcopy(info_inp)

    blank_content_val = defaultdict(list)
    blank_content_cnt = defaultdict(list)
    for i in range(len(info)-1, -1, -1):
        for j in range(len(blank)):
            if j >= i: # cannot move to right
                break
            if info[i] and info[i] <= blank[j]:
                blank_content_val[j].append(i)
                blank_content_cnt[j].append(info[i])
                blank[j] -= info[i]
                info[i] = 0
                break


    arr = list()
    for cur_ind in range(len(info)):
        cur_len = info[cur_ind]
        zero_len = starting_info[cur_ind] - cur_len
        arr.extend([cur_ind] * cur_len)
        arr.extend([0] * zero_len)

        if cur_ind < len(info)-1:
            values = blank_content_val[cur_ind]
            lengths = blank_content_cnt[cur_ind]
            if len(values):
                for v, l in zip(values, lengths):
                    arr.extend([v] * l)
                arr.extend([0] * (starting_blank[cur_ind] - sum(lengths)))
            else:
                arr.extend([0] * blank[cur_ind])

    checksum = 0
    for i, v in enumerate(arr):
        checksum += (i*v)
    return checksum


st, info, blank = parse_input('./inputs/day09.txt')
# ANSWER - 6334655979668
print(solve1(st, info, blank))

# ANSWER - 6349492251099
print(solve2(info, blank))