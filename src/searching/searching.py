def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    end = (len(arr)-1)

    found = False
    while end >= start and not found:
        middle_index = (start + end) // 2
        if arr[middle_index] == target:
            found = True
            return middle_index
        else:
            if arr[middle_index] < target:
                start = middle_index + 1 
            if arr[middle_index] > target:
                end = middle_index - 1
    return -1  # not found

