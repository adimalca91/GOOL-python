''' This is an iterative implementation of the Selection Sort Algorithm '''

def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if(lst[min_idx] > lst[j]):
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


# O(n^2)









