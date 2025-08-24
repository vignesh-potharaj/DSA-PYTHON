#BASIC LINEAR SEARCH
# Write a function linear_search that returns the index of the target
# if found, otherwise -1. Test your function with multiple arrays and targets.

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

numbers = [10, 23, 45, 70, 11, 15]
target = 70

print(linear_search(numbers, target))

# RECURSIVE LINEAR SEARCH
