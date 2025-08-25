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

def SMPI(arr, index = 0):

    new_list = []
    for index in range(len(arr)):
        if arr[index] > 0 :
            new_list.append(arr[index]) # first created a list with only positive integers
    
    smallest_number = 0
    for num in new_list:
        if num > smallest_number:
            smallest_number = num      #finding the smallest number

        
    smpi = 0
    for index in range(len(new_list)):
        if new_list[index] == smpi + 1:
            smpi = new_list[index]

    return smpi


print(SMPI(test3))