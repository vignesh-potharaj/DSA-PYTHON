# Selection sort is a sorting algorithm that repeatedly 
# finds the minimum element from the unsorted part and puts it at the beginning.

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # assume the current position is the minimum value
        min_index = i

        #checking the rest of the list of min values
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # swap the smallest value found at position 1
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort([64, 25, 12, 22, 11]))
print(selection_sort([5, 2, 8, 1, 9]))
print(selection_sort([1]))
print(selection_sort([3, 3, 3, 3]))
print(selection_sort([9, 8, 7, 6, 5]))