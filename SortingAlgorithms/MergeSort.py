def merge(left, right):
    result = []
    i = j = 0
    while (i < len(left) and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

# O(size1 + size2) = O(n)



def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst) // 2
    left_sequence = merge_sort(lst[:mid])
    right_sequence = merge_sort(lst[mid:])
    return merge(left_sequence, right_sequence)


# O(nlogn)


lst = [20,3,15,4,2,1,7,12,17]
print(lst)
print(merge_sort(lst))

