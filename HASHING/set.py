#  hashing using a set

numbers = {1, 2, 3, 5, 9}
print(numbers)

target = int(input("whats the fucking target? "))

def check_val(se, target):
    if target in se:
        return f"{target} is present"
    else:
        return f"{target} is not present"

print(check_val(numbers, target))
