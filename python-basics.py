#  Find the largest number in a list
nums = [10, 24, 76, 23, 12]

largest_num = nums[0]

for num in nums :
    if num > largest_num:
        largest_num  = num

print('largest number in the list num is',largest_num)

print(max(nums))



# Reverse a list without using the built-in reverse method

def reverse(nums):
    reversed_list = []
    for i in range(len(nums) -1, -1, -1):
        reversed_list.append(nums[i])
    return reversed_list

print(reverse(nums))


# # Check if an element exists in a list
fruits = ['apple', 'banana', 'cherry']

def searchForElement(list,element):
    for i in list:
        if i == element:
            return 'Found'
    return 'Not Found'
print(searchForElement(fruits,'banana'))
print(searchForElement(fruits,'Custard'))