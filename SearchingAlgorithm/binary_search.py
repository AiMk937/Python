# ======================================================================================
# Binary Search Algorithm
# ======================================================================================
#
# Iterative Approach
#
# ======================================================================================
# (O(log n))
# ======================================================================================

def binary_search(arr, target):
    left , right = 0 , len(arr) - 1
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [11, 12, 22, 25, 34, 64, 90]
target = 12
print(binary_search(arr, target))

# ======================================================================================
#
# Recursive Approach
#
# ======================================================================================
def binary_search_recursive(arr, target, left, right):
    if left > right:
       return -1
    mid = (left + right) // 2
    if arr[mid] == target:
       return mid
    elif arr[mid] < target:
       return binary_search_recursive(arr, target, mid+1, right)
    else:
       return binary_search_recursive(arr, target, left, mid-1)
    
arr = [11, 12, 22, 25, 34, 64, 90]
target = 25
left = 0
right = len(arr)-1
print(binary_search_recursive(arr, target, left, right))

# ======================================================================================