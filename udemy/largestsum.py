# Problem:
# Given an array of integers (positive and negative) find the largest
# continuous sum.


def largest_sum(arr):
    if not arr:
        return 0

    # Set to first element since it can be a negative number.
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum += num
        max_sum = max(current_sum, max_sum)

    return max_sum
