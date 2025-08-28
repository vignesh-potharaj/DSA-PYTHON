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
 
