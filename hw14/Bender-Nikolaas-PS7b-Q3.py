
def hindex(arr):
    minarr = min(arr)
    lenarr = len(arr)
    if lenarr < minarr:
        return lenarr
    else:
        return hindex(arr[:len(arr) - 1])
# This is the closest to the best solution I can figure out
a = [6,5,3,1,0]
print(hindex(a))