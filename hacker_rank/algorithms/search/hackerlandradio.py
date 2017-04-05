# Hackerland is a one-dimensional city with n houses, where each house i is
# located at some xi on the x-axis. The Mayor wants to install radio
# transmitters on the roofs of the city's houses. Each transmitter has a range,
# k, meaning it can transmit a signal to all houses <=k units of distance away.
#
# Given a map of Hackerland and the value of k, can you find and print the
# minimum number of transmitters needed to cover every house in the city?
# (Every house must be covered by at least one transmitter) Each transmitter
# must be installed on top of an existing house.
#
# Input Format:
# The first line contains two space-separated integers describing the
# respective values of n (the number of houses in Hackerland) and k (the range
# of each transmitter).
# The second line contains n space-separated integers describing the
# respective locations of each house (i.e., x1, x2, ..., xn).
#
# Constraints:
#   1 <= n,k <= 10^5
#   1 <= xi <= 10^5
#   There may be more than one house at the same location.
#
# Subtasks:
#   1 <= n <= 1000 for 50% of the maximum score.
#
# Output Format:
# Print a single integer denoting the minimum number of transmitters needed to
# cover all the houses.
#
# Sample Input 0
#   5 1
#   1 2 3 4 5
#
# Sample Output 0
#   2
#
# Explanation 0:
# We can cover the entire city by installing transmitters on houses at
# locations 2 and 4. Thus, we print on a new line.

n, k = map(int, raw_input().strip().split())
x = sorted(map(int, raw_input().strip().split()))

transmitters = i = 0
placed = -1
while i < n:
    if placed == -1:
        j = i + 1
        while j < n and (x[j] - x[i]) <= k:
            j += 1

        placed = x[j - 1]
        transmitters += 1
        i = j
    elif x[i] - placed > k:
        placed = -1
    else:
        i += 1

print transmitters
