#naive search, linear search function
def naive_search(target, l):
    for item in l:
        if item == target:
            return l.index(item)
    return -1

#binary search implementation
def binary_search(target, l, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1
    if high < low:
        return -1
    midpoint = len(l) // 2
    if l[midpoint] == target:
        return midpoint
    elif l[midpoint] < target:

        return binary_search(target, l[midpoint+1:high], midpoint+1, high)
    elif l[midpoint] < target:

        return binary_search(target, l[low:midpoint+1], low, midpoint-1)


list1 = [1,2,5,6,7,8,]

print(naive_search(6, list1))
print(binary_search(6, list1))

