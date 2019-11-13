import numpy as np
from random import shuffle
import time
import threading
import matplotlib.pyplot as plt


TESTS = 1000


def part(arr, p):
    eq = []
    le = []
    gr = []
    for n in arr:
        if n < p:
            le.append(n)
        if n > p:
            gr.append(n)
        if n == p:
            eq.append(n)
    # if len(eq) != 1:
    # 	print("error, it didn't find the equal to element")
    return le, eq, gr


def sort(b, c):
    # print(b, c, len(b))
    bret = []
    cret = []
    if len(b) <= 1:
        return b, c
    # Pivot for bottles is a random cap
    p = c[np.random.randint(low=0, high=len(b))]
    ble, beq, bgr = part(b, p)
    # Pivot for caps is the bottle that the random cap links up to
    p = beq[0]
    cle, ceq, cgr = part(c, p)
    sble, scle = sort(ble, cle)
    sbgr, scgr = sort(bgr, cgr)
    bret.extend(sble)
    cret.extend(scle)
    bret.extend(beq)
    cret.extend(ceq)
    bret.extend(sbgr)
    cret.extend(scgr)
    return bret, cret


def n2sort(b, c):
    bubblebottles = threading.Thread(target=bubblesort, args=(b,))
    bubblecaps = threading.Thread(target=bubblesort, args=(c,))

    # starting thread 1
    bubblebottles.start()
    # starting thread 2
    bubblecaps.start()

    # retbottles = bubblebottles.get()
    # retcaps = bubblecaps.get()

    # wait until thread 1 is completely executed
    retbottles = bubblebottles.join()
    # wait until thread 2 is completely executed
    retcaps = bubblecaps.join()

    return retbottles, retcaps


def bubblesort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


quicktimes = []
n2times = []


def testquick():
    for i in range(0, TESTS):
        bottles = [item for item in range(0, i)]
        caps = [item for item in range(0, i)]
        shuffle(bottles)
        shuffle(caps)
        start = time.time()
        sortbottles, sortcaps = sort(bottles, caps)
        quicktimes.append(time.time() - start)


def testn2():
    for i in range(0, TESTS):
        bottles = [item for item in range(0, i)]
        caps = [item for item in range(0, i)]
        shuffle(bottles)
        shuffle(caps)
        start = time.time()
        sortbottles, sortcaps = n2sort(bottles, caps)
        n2times.append(time.time() - start)


slowsort = threading.Thread(target=testn2, args=())
fastsort = threading.Thread(target=testquick, args=())

# starting thread 1
slowsort.start()
# starting thread 2
fastsort.start()

# wait until thread 1 is completely executed
slowsort.join()
# wait until thread 2 is completely executed
fastsort.join()

# sortbottles, sortcaps = sort(bottles, caps)

# print(sortbottles, sortcaps)

trials = [item for item in range(0, TESTS)]

plt.plot(trials, quicktimes, 'r--', trials, n2times, 'bs')
plt.xlabel('length of unsorted array')
plt.ylabel('time to compute')
plt.show()
