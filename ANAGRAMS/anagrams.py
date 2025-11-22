s1a = "listen"
s1b = "silent"

s2a = "triangle"
s2b = "integral"

s3a = "below"
s3b = "elbow"

# all the above are anagrams should be true

s11a = "hello"
s11b = "world"

s12a = "python"
s12b = "typhonx"

s13a = "aabb"
s13b = "ab"

s14a = "test"
s14b = "taste"
# all the above are not anagrams should be false

def isAnagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return f"is an anagram?\n{sorted(s1) == sorted(s2)}"


print("s1:", isAnagram(s1a, s1b))  # True
print("s2:", isAnagram(s2a, s2b))  # True
print("s3:", isAnagram(s3a, s3b))  # True
print("s11:", isAnagram(s11a, s11b))  # False
print("s12:", isAnagram(s12a, s12b))  # False
print("s13:", isAnagram(s13a, s13b))  # False
print("s14:", isAnagram(s14a, s14b))  # False
