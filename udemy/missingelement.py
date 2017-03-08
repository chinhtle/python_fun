import collections

# Problem:
# Consider an array of non-negative integers. A second array is formed
# by shuffling the elements of the first array and deleting a random element.
# Given these two arrays, find which element is missing in the second array.
#
# Assume there will always be one missing element in the second list.
#
# Example:
# The first array is shuffled and the number 5 is removed to construct the
# second array.
#
#   Input:
#     finder([1,2,3,4,5,6,7], [3,7,2,1,4,6])
#
#   Output:
#     5


def finder(l1, l2):
    """
    Find the missing element using the sum of two lists. Need to be careful
    of overflows. Using the built-in sum function for this.
    """
    return sum(l1) - sum(l2)


def finder2(l1, l2):
    """
    Find the missing element in a non-python specific approach.
    """
    count = collections.defaultdict(int)

    for num in l2:
        count[num] += 1

    for num in l1:
        if count[num] == 0:
            return num
        else:
            count[num] -= 1

    return None
