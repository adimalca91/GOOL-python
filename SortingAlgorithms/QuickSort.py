import random

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = random.choice(lst)
        smaller = [elem for elem in lst if elem < pivot]
        equal = [elem for elem in lst if elem == pivot]
        greater = [elem for elem in lst if elem > pivot]
        return quick_sort(smaller) + equal + quick_sort(greater)

# Worst-case: O(n^2)
# Best-case: O(nlogn)
# Average-case: O(nlogn)
