# Filter a list of strings to get only those containing "a

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if 'a' in x]

print(newlist)

# Given a list of integers, create a new list containing 
# only the squares of the odd numbers from the original list.

numbers = [1, 2, 3, 4, 5, 6]
square_of_odd =  [x **2 for x in numbers if x % 2 != 0]
print(square_of_odd)

# Given a list of words, create a new list 
# containing only the words that are longer than 4 characters, converted to uppercase.
words = ["apple", "dog", "banana", "cat", "elephant"]
longer_than_4 = [x.upper() for x in words if len(x) > 4]

print(longer_than_4)


# converting words longer than 4 to uppercase and others to lowercase
longer_than_4_ul = [x.upper() if len(x) > 4 else x for x in words]
print(longer_than_4_ul)


