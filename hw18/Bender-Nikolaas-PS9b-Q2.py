import random
hw = [2, 7, 9, 3, 5, 1]

# Thank you alex for helping me on this question
# my previous solution was not correct, howevery this should be
def optim(arr):
    best_hws = []
    for i in range(len(arr)):
        if i == 0:
            best_hws.append(arr[i])
        elif i == 1:
            best_hws.append(max(arr[i], arr[i - 1]))
        else:
            best_hws.append(max(best_hws[i - 2] + arr[i], best_hws[i - 1]))
    return best_hws[-1]


def sum_evens(arr):
    i = 0
    sum_ele = 0
    while i < len(arr):
        sum_ele += arr[i]
        i += 2
    return sum_ele


def sum_odds(arr):
    i = 1
    sum_ele = 0
    while i < len(arr):
        sum_ele += arr[i]
        i += 2
    return sum_ele


def DP_table(arr):
    sub_problems = []
    for i in range(1, len(arr)):
        sub_arr = arr[:i]
        sub_problems.append(optim(sub_arr))
    print("part c:", sub_problems)


print("optimal value ", optim(hw))

num_hw = random.randint(0, 50)
hw_assgs = []
for i in range(num_hw):
    hw_assgs.append(random.randint(0, 50))

print(hw_assgs)
print("sum even elements", sum_evens(hw_assgs))
print("sum odd elements", sum_odds(hw_assgs))
# for some reason its not computing what should be t he last element of the dp table
print("part b: ", optim(hw_assgs))
DP_table(hw_assgs)
