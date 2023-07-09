
# Ascending Order (from lowest to highest)

def iterative_bubble_sort(lst):
    for i in range(len(lst)-1):
        for k in range(len(lst)-1-i):
            if lst[k] > lst[k+1]:
                temp = lst[k+1]
                lst[k+1] = lst[k]
                lst[k] = temp
    print(lst)

iterative_bubble_sort([1,5,3,6,2,9,4,8,7])


# Descending Order (from highest to lowest)

def iterative_bubble_sort_descending(lst):
    for i in range(len(lst)-1):
        for k in range(len(lst)-1-i):
            if lst[k] < lst[k+1]:
                temp = lst[k+1]
                lst[k+1] = lst[k]
                lst[k] = temp
    print(lst)

iterative_bubble_sort_descending([10,5,3,6,2,9,4,8,7])