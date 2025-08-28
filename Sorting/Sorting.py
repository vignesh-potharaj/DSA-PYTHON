# BUBBLE SORT

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j +1] = arr[j +1], arr[j]
    return arr

nums = [5, 2, 8, 3, 1]
arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble_sort(nums))
print(bubble_sort(arr))

# Write code to sort a list of strings by their lengths.

words = ["apple", "banana", "fig", "cherry", "date"]

def sort_word_by_length(arr):
    return sorted(arr, key=len)

print(bubble_sort(words))
print(sort_word_by_length(words))

#  Sort a list of tuples by their second element

pairs = [(1, 3), (3, 2), (2, 1), (5, 4)]
def sort_by_second_element(tup):
    return sorted(tup, key = lambda x:x[1])

print(sort_by_second_element(pairs))