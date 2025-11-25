# reverse string palindrome checking come

def palindromeCheck(str):
    if (str[::-1] == str):
        return "Yes this is a palindrome"    
    return "No this is not a palindrome"

print(palindromeCheck("racecar"))
print(palindromeCheck("hello"))
print(palindromeCheck("a"))
print(palindromeCheck("madam"))
print(palindromeCheck("12321"))