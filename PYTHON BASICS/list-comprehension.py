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


# Given a list of lists of integers, create a new flat 
# list containing the squares of all even numbers from the sublists.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
square_of_even_matrix = [ x**2 for sublist in matrix for x in sublist if x % 2 == 0]

print(square_of_even_matrix)


# Given two lists of numbers, create a new list containing the product of all pairs 
# (one number from each list) where the product is an even number.

list1 = [1, 2, 3]  
list2 = [4, 5, 6]

Even_Products = [x*y for x in list1  for y in list2 if x*y %2 == 0]

print(Even_Products)

# Given a list of sentences (strings), create a new list containing 
# the first letter of each word, but only for the words that have more than 3 letters.

sentences = [
    "The quick brown fox",
    "jumps over the lazy dog",
    "Python programming is fun"
]

first_letter = [x[0] for sent in sentences for x in sent.split() if len(x) > 3]
print(first_letter)

# Given a list of strings called phrases, create a new list containing only palindromic words 
# (words that read the same forwards and backwards, case-insensitive) from all the phrases, converted to lowercase.
# Ignore any single-character words.

phrases = [
    "Madam Arora teaches malayalam",
    "Level done, refer racecar stats",
    "Python is fun"
]

palindromic_words = [x.lower() for sent in phrases for x in sent.split() if len(x) > 3 and x.lower() == x[::-1].lower()]
print(palindromic_words)

# Given a list of dictionaries called data, where each dictionary contains a person's '
# 'name and a list of integers as their scores, create a new list of tuples where each tuple '
# 'consists of the person's name and their average score. Only include people whose average score is above 70.

data = [
    {"name": "Alice", "scores": [88, 76, 92]},
    {"name": "Bob", "scores": [65, 59, 72]},
    {"name": "Charlie", "scores": [91, 85, 100]}
]
name_and_average = [(person['name'], avg)
                    for person in data 
                    if (avg :=sum(person["scores"]) / len(person["scores"])) > 70]

print(name_and_average)


# Given a list of integers nums, create a new list containing strings that classify each number as follows:
# If the number is divisible by 3, the string should be "Fizz".
# If the number is divisible by 5, the string should be "Buzz".
# If the number is divisible by both 3 and 5, the string should be "FizzBuzz".
# Otherwise, include the number itself as a string.

nums = list(range(1, 21))

FizzBuzz = ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 
                else 'Fizz' if x % 3 == 0
                else 'Buzz' if x % 5 == 0
                else str(x)
                for x in nums 
     ]

print(FizzBuzz)

# Given a list of mixed data types (integers, strings, floats, etc.), create a new list 
# containing only the integers that are prime numbers.

mixed_list = [2, "hello", 3.5, 5, 7, 8, "world", 11, 13, 15, 17, 19, "python"]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_list = [x for x in mixed_list if isinstance(x, int) and is_prime(x)]

print(prime_list)