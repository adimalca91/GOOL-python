
def iterative_binary_search(lst, x):
    low = 0
    mid = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2 # floor division

        if x > lst[mid]:
            low = mid + 1
        elif x < lst[mid]:
            high = mid - 1
        else:
            return mid

    return -1


lst = [1,2,3,4,5,6,9,12,45,55,62,73]
x = 6

print(iterative_binary_search(lst, x))