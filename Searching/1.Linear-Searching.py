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


# Largest odds number in string

def largestOdd(str):
    result = 0
    odds = []
    for i in range(len(str)):
        if int(str[i]) % 2 != 0:
            odds.append(str[i])
            
    if len(odds) == 0:
        result = "no odd numbers in the string"

    for j in range(0,len(odds) - 1):
        if odds[j] < odds[j + 1]:
            result = odds[j + 1]
    return result

# Test cases to run:
print("Test 1:")
print(largestOdd("123456789"))

print("\nTest 2:")
print(largestOdd("2468")) 

print("\nTest 3:")
print(largestOdd("13579"))

