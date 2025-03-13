# Find the Largest element in an array

# Problem Statement: Given an array, we have to find the largest element in the array.

# Example 1:
# Input:
#  arr[] = {2,5,1,3,0};
# Output:
#  5
# Explanation:
#  5 is the largest element in the array. 

# Example2:
# Input:
#  arr[] = {8,10,5,7,9};
# Output:
#  10
# Explanation:
#  10 is the largest element in the array. 

import array as arr

arr1 = arr.array('i',[2,5,1,3,0])
large1=max(arr1)
print(large1)

arr2 = arr.array('i', [8,10,5,7,9])
large2=max(arr2)
print(large2)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x< pivot]
        middle = [x for x in arr if x==pivot]
        right = [x for x in arr if x > pivot] 
        return quick_sort(left) + middle + quick_sort(right)

arr3 = [2,5,1,3,0]  
arr4 = [8,10,5,7,9]

sorted_arr3 = quick_sort(arr3)
sorted_arr4 = quick_sort(arr4)

print(sorted_arr3)
print(sorted_arr4)

print(sorted_arr3[-1])
print(sorted_arr4[-1])
