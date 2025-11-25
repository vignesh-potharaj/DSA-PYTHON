# Insertion sort is a sorting algorithm that builds the final sorted 
# array one item at a time by inserting each element into its correct position.

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1

        while ( j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr

print(insertion_sort([64, 25, 12, 22, 11]))
print(insertion_sort([5, 2, 8, 1, 9]))
print(insertion_sort([1]))
print(insertion_sort([3, 3, 3, 3]))
print(insertion_sort([9, 8, 7, 6, 5]))