# Problem: Given a list of numbers and a target number, k, find unique
# pairs where the sum equals k.


def pairsum(num_list, k):
    if num_list < 2:
        return 0

    # Use sets instead of arrays for faster search times.
    seen = set()
    output = set()

    for num in num_list:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((num, target))

    print len(output)
