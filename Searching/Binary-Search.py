numbers = [10, 20, 30, 40, 50, 60]

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            found = True
            break
        elif numbers[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return found

print(binarySearch(numbers, 30))