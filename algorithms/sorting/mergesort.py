def mergesort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) / 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    merged = []
    while len(left) and len(right):
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    # Append any remaining elements that were not added
    merged += left
    merged += right

    return merged


a = [1, 3, 40, 20, 100, 50, 4, 20]

print "Before sort:", a
a = mergesort(a)
print "After sort:", a
