# Find the smallest element in an array

# Problem Statement: Given an array, we have to find the smallest element in the array.

# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 0
# Explanation: 0 is the smallest element in the array. 

# Example2: 
# Input: arr[] = {8,10,5,7,9};
# Output: 5
# Explanation: 5 is the smallest element in the array.

import array as arr
arr1 = arr.array('i', [2,5,1,3,0])
small1=min(arr1)
print(small1)


arr2 = arr.array('i', [8,10,5,7,9])
small2=min(arr2)
print(small2)

