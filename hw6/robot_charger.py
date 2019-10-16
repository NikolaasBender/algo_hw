def chargey_boi(k, chargers):
    chg_use = []
    new_k = k
    tmp = 0
    for dist in chargers:
        if dist > tmp and dist < new_k:
            tmp = dist
        if dist > new_k:
            new_k = tmp + k
            chg_use.append(tmp)
            if dist > tmp and dist < new_k:
                tmp = dist
    return chg_use


print(chargey_boi(40, [0, 20, 37, 54, 70, 90]))
print(chargey_boi(20, [0, 18, 21, 24, 37, 56, 66]))
print(chargey_boi(20, [0, 10, 15, 18]))


def rockie_team(n, lst):
    ret = []
    goal = n
    i = len(lst) - 1
    while i > -1:
        if lst[i] < goal or lst[i] == goal:
            ret.append(lst[i])
            goal = goal - lst[i]
        i -= 1

    return ret


print(rockie_team(5, [1, 2, 4, 8, 16]))
# for i in range(32):
#     check = rockie_team(i, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     print(check, i, sum(check))

print(rockie_team(1, [0, 1]))
print(rockie_team(1, [-1, 0, 1]))

