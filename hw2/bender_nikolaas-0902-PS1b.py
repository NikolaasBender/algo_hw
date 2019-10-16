from random import shuffle
import time
import matplotlib.pyplot as plt


def shuffle_count(n):
    A = [[i] for i in range(n+1)]
    shuffle(A)
    flips = 0
    # Get a number to check
    for i in range(0, len(A)):
        num = A[i]
        # loop through all numbers after the index of num to check for flips
        for j in range(i, len(A)):
            if A[j] > num:
                flips += 1

    return flips

tests = 15

flips_data = []
times_data = []
for i in range(tests):
    start = time.time()
    flips = shuffle_count(2**i)
    end = time.time() - start
    flips_data.append(flips)
    times_data.append(end)
print(flips_data)
print(times_data)

test_range = list(range(0, tests))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
axes[0].plot(test_range, flips_data)
axes[0].set_xlabel("input array length")
axes[0].set_ylabel("number of flips found (x10,000,000)")
axes[0].set_title("flip data")
axes[1].plot(test_range, times_data)
axes[1].set_xlabel("input array length")
axes[1].set_ylabel("time to calcualte (s)")
axes[1].set_title("time data")
plt.savefig('hw2_data.png')
plt.show()
