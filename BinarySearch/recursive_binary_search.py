def recursive_binary_search(lst, low, high, x):

    if low <= high:

        mid = (low+high) // 2

        # Base Case
        if x == lst[mid]:
            return mid
        elif x > lst[mid]:
            return recursive_binary_search(lst, mid+1, high, x)
        else:
            return recursive_binary_search(lst, low, mid-1, x)

    else:
        return -1


lst = [1,2,3,4,5,6,9,12,45]
low = 0
high = 8
x = 6
print(recursive_binary_search(lst, low, high, x))
