# ======================================================================================
# Linear Search Algorithm
# ======================================================================================
#
# Iterative Approach
#
# ======================================================================================
# Best case (O(1)) → If the target is at the first position.
# Worst case (O(n)) → If the target is at the last position or not in the list.
# ======================================================================================

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

arr2 = [64, 34, 25, 12, 22, 11, 90]
target = 90
print(linear_search(arr2, target))

# ======================================================================================
#
# Recursive Approach
#
# ======================================================================================

def linear_search_recursive(arr, target, index=0):
    if index >= len(arr):
        return "Not present"
    if arr[index] == target:
        return index
    return linear_search_recursive(arr, target, index+1)

arr2 = [64, 34, 25, 12, 22, 11, 90]
target = 91
print(linear_search_recursive(arr2, target))

# ======================================================================================