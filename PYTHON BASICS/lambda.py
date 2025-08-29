# Lambda in Python is a way to create small anonymous functions on the fly, typically for 
# short-term use. A lambda function can take any number of arguments but only consists of 
# a single expression, which it evaluates and returns. It is defined using the syntax:

#           lambda arguments: expression


# Task 1: Create a lambda function that adds 5 to a 
# number and use it to add 5 to the numbers 3 and 10.

print((lambda x: x + 5)(3))
print((lambda x: x + 5)(10))

# Task 2: Create a lambda function that 
# multiplies two numbers and test it with 4 and 7.

multiply = lambda x, y: x*y

print(multiply(4, 7))
print(multiply(4, 5))
print(multiply(3, 7))

# Task 3: Use lambda with the map() function to 
# multiply each element in the list [1, 2, 3, 4] by 3.

list1 = [1, 2, 3, 4]
tripled = list(map(lambda x: x * 3,list1))

print(tripled)

list2 = [10, 15, 20, 25, 30]

filter_even = list(filter(lambda x: x % 2 ==0,list2))
print(filter_even)

# Task 5: Sort a list of strings based on their 
# length using sorted() and a lambda function as the key.

list3 = ["apple", "banana", "pear", "kiwi", "grape"]

def sort_on_length(arr):
    return sorted(arr ,key= lambda x: len(x))

print(sort_on_length(list3))

# Task 6: Use reduce() and a lambda function to calculate the factorial of 5 (i.e., 5!)

# You will need to import reduce from functools to solve this.

from functools import reduce

def factorial(n):
    if n == 0:
        return 1
    return reduce(lambda x,y : x*y,range(1, n + 1))

print(factorial(5))
print(factorial(4))
print(factorial(3))
print(factorial(2))
print(factorial(1))
print(factorial(0))

# Task 7: Use a lambda function with sorted() to 
# sort a list of tuples based on the second item in each tuple.

list_of_tuples = [(1, 3), (2, 2), (4, 1), (3, 4)]

def sort_on_second_item(arr):
    return sorted(arr, key=lambda x: x[1])

print(sort_on_second_item(list_of_tuples))


# Task 8: Use a lambda function to group a list of words by 
# their first letter using sorted() and the groupby() function from itertools.

from itertools import groupby
words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado"]
words_sorted = sorted(words, key=lambda x: x[0])

grouped = groupby(words_sorted, key= lambda x:x[0])

for key, group in grouped:
    print(key, list(group))

# Task 9: Given a list of dictionaries, use a 
# lambda and sorted() to sort the dictionaries by a specific key.

students = [
    {'name': 'Tom', 'score': 85},
    {'name': 'Emma', 'score': 92},
    {'name': 'Alex', 'score': 78},
    {'name': 'Sophia', 'score': 90}
]

sorted_students = sorted(students, key= lambda x: x['score'], reverse=True)

print(sorted_students)

# Task 10: Use a lambda with map() and two lists to add corresponding elements together.

a = [2, 4, 6, 8]
b = [1, 3, 5, 7]

a_and_b = list(map(lambda x,y: x + y,a, b))
print(a_and_b)

# Task 11: Use a lambda function with filter() to extract all strings that start 
# with the letter "a" from a list of strings.

words = ["apple", "banana", "apricot", "blueberry", "cherry", "avocado", "grape"]

filtered_words = list(filter(lambda x: x[0] == 'a',words))

print(filtered_words)


# Task 12: Use a lambda function with map() to convert a list of strings to uppercase.

fruits = ["apple", "banana", "cherry", "date"]

Upper_fruits = list(map(lambda x: x.upper(),fruits))

print(Upper_fruits)

# (Task 13):
# Use a lambda with filter() to get all numbers greater than 10 from the list:

numbers = [4, 11, 7, 15, 3, 20, 8]

greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(greater_than_10)

#  (Task 14):Use a lambda with map() to square each number in the list:

numbers = [1, 2, 3, 4, 5]
square_numbers = list(map(lambda x: x**2, numbers))
print(square_numbers)

#  (Task 15):Use a lambda with filter() to extract all odd numbers from the list:
numbers = [10, 15, 22, 33, 40, 55, 60]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#  (Task 16):Use a lambda with map() to create a new list where each element is the triple 
# of the corresponding element in the list:

numbers = [1, 3, 5, 7, 9]

tripled_numbers = list(map(lambda x: x*3,numbers))

print(tripled_numbers)
