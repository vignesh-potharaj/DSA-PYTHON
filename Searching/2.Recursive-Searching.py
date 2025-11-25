# RECURSIVE LINEAR SEARCH

#1a. Write a function that returns 
# the index of the first occurrence of a target in a list. If the target is not found, return -1.


numbers = [10, 23, 45, 70, 11, 15]
target = 70



def recursive_linear_search(arr, target, index=0):
    if index == len(arr):
        return -1
    if arr[index] == target:
        return index
    return recursive_linear_search(arr, target , index + 1)

target1 = 23
target2 = 90

print(recursive_linear_search(numbers, target1))
print(recursive_linear_search(numbers, target2))



# 1b.Given an array nums and a value val, remove all 
# instances of that value in-place and return the new length. The order of elements can be changed.

nums = [3, 2, 2, 3]
val = 3

def Search_and_Remove(arr, val, index = 0):
    if index == len(arr):
        return []
    rest = Search_and_Remove(arr, val, index + 1)
    
    if arr[index] == val:
        return rest
    else:
        return [arr[index]] + rest

print(Search_and_Remove(nums, val))


# Given an unsorted integer array, find the smallest missing positive integer.

test3 = [3, 4, -1, 1]
test4 = [7, 8, 9, 11, 12]
test5 = [1, 2, 0]

def SMPI(arr):
    positives = set()
    for x in arr:
        if x > 0:
            positives.add(x)
    
    i = 1

    while True:
        if i not in positives:
            return i 
        else:
            i += 1

print(SMPI(test3))
print(SMPI(test4))
print(SMPI(test5))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          