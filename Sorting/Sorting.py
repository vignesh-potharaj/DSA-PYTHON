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


# Given a list of dictionaries representing students 
# with keys name and score, sort the list by score in descending order.

students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 95},
]

Sort_by_Score = sorted(students,key= lambda x: x['score'], reverse= True)

print(Sort_by_Score)

# Sort a list of tuples by the sum of elements in each tuple.

tuples_list = [(1, 2), (4, 0), (2, 2), (3, 3)]

sorted_list = sorted(tuples_list, key=sum)

print(sorted_list)

# Custom sort: Sort strings by the number of vowels

words = ["banana", "apple", "cherry", "date"]

sort_by_vowels = sorted(words, key= lambda x:sum(char in 'aeiou' for char in x.lower()))

print(sort_by_vowels)

#  Sort a list of numbers but place odd numbers first (keeping their order)

# Sort a list of numbers such that all odd numbers come before the even numbers, 
# while preserving the original relative order of odds and evens.

numbers = [5, 2, 3, 4, 1, 6]
def odd_first(arr):
    odd = [x for x in arr if x % 2 != 0]
    even = [x for x in arr if x % 2 == 0]
    return odd + even
print(odd_first(numbers))

