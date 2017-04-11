def quicksort_helper(arr, low, high):
    if low >= high:
        return

    pivot = high

    wall = i = 0
    while i < high:
        if arr[i] < arr[pivot]:
            arr[wall], arr[i] = arr[i], arr[wall]
            wall += 1

        i += 1

    arr[wall], arr[pivot] = arr[pivot], arr[wall]

    quicksort_helper(arr, low, wall - 1)
    quicksort_helper(arr, wall, high)


def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)


arr = [100, 20, 10, 2000, 5, 50000, 30, 1]

print "Before sort:", arr
quicksort(arr)
print "After sort:", arr
