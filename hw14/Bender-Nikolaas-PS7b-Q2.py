import numpy as np
from random import shuffle
import matplotlib.pyplot as plt
import time


TESTS = 100

# I spent a day bashing my head against this and Alex ended up helping me out
# read my comments so you know I understand whats going on.
# Thank you alex for the help, you have saved my ass



def mergeSort(A, p, r):
    count = 0
    if p < r:
        q = (p + r)//2
        # divide more on the lower section of A
        count += mergeSort(A, p, q)
        # divide more on the upper section of A
        count += mergeSort(A, q + 1, r)
        # combine lower and upper sections
        count += merge(A, p, q, r)
    return count


def merge(A, p, q, r):
    # A is the original array,
    # p is the pivot index,
    # q is the left index,
    # r is the right index

    count = i = j = 0
    # K is the pivot location
    k = p
    low = []
    high = []

    # Create the lower array
    for x in range(p, q+1):
        low.append(A[x])
    # Created the upper array
    for x in range(q+1, r+1):
        high.append(A[x])

    # This is where the actual sorting happens
    while i < (q - p + 1) and j < (r - q):
        # If the element doesn't need to be moved then its put right back into A
        if low[i] <= high[j]:
            A[k] = low[i]
            i += 1
        else:
            A[k] = high[j]
            # the i-th element and all following elements in low are flips
            # high will slot into here in low so we have to count
            # all of those flips. This is the really clever bit of counting
            count += (q - p + 1 - i)
            j += 1
        k += 1
    while i < (q - p + 1):
        A[k] = low[i]
        i += 1
        k += 1
    while j < (r - q):
        A[k] = high[j]
        j += 1
        k += 1
    return count


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def shuffle_count(A):
    flips = 0
    # Get a number to check
    for i in range(0, len(A)):
        num = A[i]
        # loop through all numbers after the index of num to check for flips
        for j in range(i, len(A)):
            if A[j] < num:
                flips += 1

    return flips


n2swaps = []
n2times = []
lognswaps = []
logtimes = []

for i in range(1, TESTS + 1):
    n = [item for item in range(1, i + 1)]
    shuffle(n)
    sortedlist = shuffle_count(n)
    # print(sortedlist)
    start = time.time()
    n2swaps.append(sortedlist)
    n2times.append(time.time() - start)

    startlog = time.time()
    ms = mergeSort(n, 0, len(n)-1)
    logtimes.append(time.time() - startlog)
    # print(sortedlist)
    lognswaps.append(ms)


# print("n2swaps", n2swaps)
# print("lognswaps", lognswaps)
if n2swaps != lognswaps:
    print("your sorting algorithms didn't agree")
else:
    print("your sorting algorithms agreed")

# sortbottles, sortcaps = sort(bottles, caps)

# print(sortbottles, sortcaps)

trials = [item for item in range(0, TESTS)]
plt.plot(trials, n2times, label="n^2 times", linestyle=":")
plt.plot(trials, logtimes, label="logn times", linestyle="-")
plt.plot(trials, n2swaps, label="n^2 swaps", linestyle="-.")
plt.plot(trials, lognswaps, label="logn swaps", linestyle="--")
plt.legend(loc='upper left')
# plt.show()

plt.savefig("logflips.png")
